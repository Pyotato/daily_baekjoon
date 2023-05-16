{
  class Queue {
    arr: Array<number>;
    ans: Array<number>;
    length: number;
    head: number;
    tail: number;

    constructor() {
      this.arr = [];
      this.ans = [];
      this.length = this.arr.length;
      this.head = -1;
      this.tail = -1;
    }
    push(item: number) {
      this.arr.push(item);
      this.length++;
    }
    front() {
      this.head = this.arr[0];
      this.length === 0 ? this.ans.push(-1) : this.ans.push(this.head);
    }
    size() {
      this.ans.push(this.length);
    }
    back() {
      this.tail = this.arr[this.length - 1];
      this.length === 0 ? this.ans.push(-1) : this.ans.push(this.tail);
    }
    empty() {
      this.length === 0 ? this.ans.push(1) : this.ans.push(0);
    }
    pop() {
      if (this.length === 0) {
        this.ans.push(-1);
      } else {
        this.ans.push(this.head);
        this.arr.splice(0, 1);
      }
    }
  }

  const N: string | null = prompt("명령의 개수를 입력해주세요.");
  const n: number = N ? parseInt(N) : 0;
  const q_cmds: Array<string> = [];
  if (n > 0) {
    for (let i = 0; i < n; i++) {
      const cmd: string | null = prompt(`${i + 1}번째 명령을 입력해주세요.`);
      cmd && q_cmds.push(cmd);
    }
    const q = new Queue();
    q_cmds.map((v: string) => {
      const splt_v: Array<string> = v.split(" ");
      splt_v[0] === "push"
        ? q.push(parseInt(splt_v[1]))
        : splt_v[0] === "front"
        ? q.front()
        : splt_v[0] === "back"
        ? q.back()
        : splt_v[0] === "empty"
        ? q.empty()
        : splt_v[0] === "pop"
        ? q.pop()
        : console.log("명령값이 부적절합니다.");
    });
    q.ans.map((v) => console.log(v));
  } else {
    console.log("입력값이 부적합합니다.");
  }
}
/*
* test1

15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

* result
1
2
2
0
1
2
-1
0
1
-1
0
3

*/
