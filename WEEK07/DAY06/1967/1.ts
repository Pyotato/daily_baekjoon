{
  const n: string | null = prompt("노드의 개수를 입력해주세요.");
  const error_msg = () => console.log("잘못된 입력값입니다.");

  if (n) {
    const nodes_count: number = parseInt(n);
    const tree: Map<number, number[][]> = new Map(); // tree 구조 (연결된 간선, 간선간의 거리)을 담은 이중 배열
    const instructions: number[][] = []; // 간선 정보 담은 이중배열

    for (let i = 1; i < nodes_count; i++) {
      const temp: string | null = prompt(`${i}번째 간선의 정보를 알려주세요.`);
      temp
        ? instructions.push(temp.split(" ").map((v) => parseInt(v)))
        : error_msg();
    }

    // 트리 만들기
    instructions.forEach((v) => {
      const [p, c, w] = v;
      if (tree.has(p)) {
        const edges = tree.get(p) as number[][];
        edges.push([c, w]);
      } else {
        tree.set(p, [[c, w]]);
      }
      if (tree.has(c)) {
        const edges = tree.get(c) as number[][];
        edges.push([p, w]);
      } else {
        tree.set(c, [[p, w]]);
      }
    });

    let max_node: number = -1;
    let max_distance: number = 0;

    const bfs = (s_node: number): number => {
      const visited: Array<number> = new Array(nodes_count + 1).fill(-1);
      const q: Array<Array<number>> = [];
      q.push([s_node, 0]);
      visited[s_node] = 0;
      while (q.length > 0) {
        const child = q.shift() as Array<number>;
        const [n, d] = child;
        const curr = tree.get(n) as Array<Array<number>>;
        if (!curr) {
          continue;
        }
        for (const [e, w] of curr) {
          if (visited[e] === -1) {
            visited[e] = d + w;
            q.push([e, d + w]);
            if (max_distance < d + w) {
              max_distance = d + w;
              max_node = e;
            }
          }
        }
      }
      return max_distance;
    };

    if (instructions.length === 1) {
      console.log(0);
    } else {
      bfs(1);
      bfs(max_node);
      console.log(max_distance);
    }
  } else {
    error_msg();
  }
}
