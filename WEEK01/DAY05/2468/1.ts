interface Graph {
  items: Array<Array<number>>;
  count: number;
  max_num_arr: Array<number>;
  max_num: number;
  visited?: Array<Array<number>>;
  x_y_idx?: Array<number>;
  x?: number;
  y?: number;
}

const directions = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

const dfs = (
  dq: Array<Array<number>>,
  a: Graph["items"],
  fld: Graph["items"],
  v: Graph["items"]
) => {
  while (dq.length > 0) {
    const popLeft: Array<number> = dq[0];
    let x: number = popLeft[0];
    let y: number = popLeft[1];
    dq.splice(0, 1);
    for (let k = 0; k < 4; k++) {
      let nx = x + directions[k][0];
      let ny = y + directions[k][1];
      if (0 <= nx && nx < a.length && ny >= 0 && ny < a.length) {
        if (fld[nx][ny] == 1 && v[nx][ny] === 0) {
          v[nx][ny] = 1;
          dq.push([nx, ny]);
        }
      }
    }
  }
};

//높이그래프 순회하면서 높이에 따른 잠긴 지역표시
const sunk = (area: Graph["items"], max_height: Graph["max_num"]) => {
  let h: number = max_height - 1;
  let flooded: Graph["items"];
  const ans_arr: Array<number> = [];
  while (h >= 0) {
    //잠김 = 0, 잠기지 않음 =1
    flooded = area.map((v) => {
      return v.map((itm) => {
        return itm > h ? 1 : 0;
      });
    });
    h--;
    const visited: Graph["visited"] = [...area].map((v) => [...v].fill(0));
    let cnt: number = 0;
    for (let i = 0; i < area.length; i++) {
      for (let j = 0; j < area.length; j++) {
        if (flooded[i][j] == 1 && visited[i][j] == 0) {
          let q: Array<Array<number>> = [];
          q.push([i, j]);
          dfs(q, area, flooded, visited);
          visited[i][j] = 1;
          cnt++;
        }
      }
    }
    ans_arr.push(cnt);
  }

  return Math.max(...ans_arr);
};
//input값들 받아오기 & 에러처리
const sol = () => {
  const n: string | null = prompt("지역의 개수 NxN개에서 N을 입력해주세요:");
  const N: Graph["count"] | null = n ? parseInt(n) : null;
  const max_arr: Graph["max_num_arr"] = [];
  const heights: Graph["items"] = [];
  let max_a: Graph["max_num"] = 1;
  if (n && N && !n.includes(" ")) {
    for (let i = 0; i < N; i++) {
      const h: string | null = prompt(`${i + 1}줄에서 지역의 높이`);
      h ? heights.push(h.split(" ").map((v) => parseInt(v))) : null;
      max_arr.push(Math.max(...heights[i]));
      if (heights[i].length !== N) {
        return console.log("구역의 높이 개수가 불일치 합니다.");
      }
    }
    if (heights.length === N && heights.map((v) => v.length == N)) {
      max_a = Math.max(...max_arr);
    } else {
      return console.log("구역의 높이 개수가 불일치 합니다.");
    }
  } else {
    console.log("지역의 개수가 부적합합니다.");
    return;
  }
  let count: number = 0;

  console.log(sunk(heights, max_a));
};

sol();
