{
  class deQue {
    arr: Array<number>;
    ans: Array<number>; //문제 풀이를 위해 출력 담을 배열
    head: number;
    tail: number;

    constructor() {
      this.arr = [];
      this.ans = [];
      this.head = -1;
      this.tail = -1;
    }
    push_front(item: number) {
      this.arr.splice(0, 0, item);
    }
    push_back(item: number) {
      this.arr.push(item);
    }
    pop_front() {
      if (this.arr.length === 0) {
        this.ans.push(-1);
      } else {
        this.ans.push(this.head);
        this.arr.splice(0, 1);
      }
    }
    pop_back() {
      if (this.arr.length === 0) {
        this.ans.push(-1);
      } else {
        this.ans.push(this.head);
        this.arr.pop();
      }
    }
    size() {
      this.ans.push(this.arr.length);
    }
    empty() {
      this.arr.length === 0 ? this.ans.push(1) : this.ans.push(0);
    }
    front() {
      this.head = this.arr[0];
      this.arr.length === 0 ? this.ans.push(-1) : this.ans.push(this.head);
    }
    back() {
      this.tail = this.arr[this.arr.length - 1];
      this.arr.length === 0 ? this.ans.push(-1) : this.ans.push(this.tail);
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
    const deq = new deQue();
    q_cmds.map((v: string) => {
      const splt_v: Array<string> = v.split(" ");
      splt_v[0] === "push_front"
        ? deq.push_front(parseInt(splt_v[1]))
        : splt_v[0] === "push_back"
        ? deq.push_back(parseInt(splt_v[1]))
        : splt_v[0] === "front"
        ? deq.front()
        : splt_v[0] === "back"
        ? deq.back()
        : splt_v[0] === "empty"
        ? deq.empty()
        : splt_v[0] === "pop_front"
        ? deq.pop_front()
        : splt_v[0] === "pop_back"
        ? deq.pop_back()
        : console.log("명령값이 부적절합니다.");
    });
    deq.ans.map((v) => console.log(v));
  } else {
    console.log("입력값이 부적합합니다.");
  }
}
/*
  * test1
  
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
  
  * result
 2
1
2
0
2
1
-1
0
1
-1
0
3

---

22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back

result

-1
-1
-1
-1
1
1
2
2
333
10
10
333
20
1234
1234
20
  
  */
