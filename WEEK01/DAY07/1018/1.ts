{
  const board_size: string | null = prompt("체스판의 크기 N,M을 입력해주세요");
  const N: number = board_size ? parseInt(board_size.split(" ")[0]) : 0;
  const M: number = board_size ? parseInt(board_size.split(" ")[1]) : 0;

  if (N >= 8 && N <= 50) {
    const chess: Array<Array<number>> = [];
    for (let i = 0; i < N; i++) {
      const row = prompt(
        `${i + 1}번째 줄에 해당되는 체스판색들을 입력해주세요`
      );
      if (row && row.length != M) {
        console.log(
          `${i + 1}번째 줄에 해당되는 체스판 색의 개수가 부족합니다.`
        );
        break;
      } else {
        if (row) {
          row.includes("B") ||
            (row.includes("W") &&
              chess.push(row.split("").map((v) => (v == "B" ? 1 : 0))));
        } else {
          console.log(`${i + 1}번째 줄에 해당되는 체스판 색이 부적절합니다.`);
        }
      }
    }
    console.log(chess);
    //체스판 순회하면서 0시작 1시작 조건으로 바뀌는 수 구하기
    const c_start = (
      n: number,
      m: number,
      start: number,
      end: number
    ): number => {
      let count: number = 0;
      for (let i = n; i < n + 8; i++) {
        if (i % 2 === 0) {
          //짝수행
          for (let j = m; j < m + 8; j++) {
            if (j % 2 === 0) {
              chess[i][j] === start ? (count = count + 1) : count;
            } else {
              chess[i][j] === end ? (count = count + 1) : count;
            }
          }
        } else {
          //홀수행
          for (let j = m; j < m + 8; j++) {
            if (j % 2 === 0) {
              chess[i][j] === end ? (count = count + 1) : count;
            } else {
              chess[i][j] === start ? (count = count + 1) : count;
            }
          }
        }
      }

      return count;
    };

    //체스판 8X8크기로 짜르면서 최소 바꾼 횟수를 배열에 넣어 배열 최소를 리
    const clr_board = (n: number, m: number): number => {
      const ans: Array<number> = [];
      for (let i = 0; i < N - 7; i++) {
        for (let j = 0; j < M - 7; j++) {
          ans.push(c_start(i, j, 0, 1));
          ans.push(c_start(i, j, 1, 0));
        }
      }
      return Math.min(...ans);
    };
    console.log(clr_board(N, M));
  } else {
    console.log("체스판 크기 입력값이 부적절합니다.");
  }
}
/*

* test1
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

result: 1

---

* test3
8 8
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB

result: 0
---

* test2
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB

result: 12
---

* test2
10 10
BBBBBBBBBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBBBBBBBBB
result: 0

---

* test2
9 23
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW

result: 31

---

10 10
BBBBBBBBBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBBBBBBBBB

result : 0
--

* test2

8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWWWB
BWBWBWBW

result: 2 

---

* test2
11 12
BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW

result: 15


*/
