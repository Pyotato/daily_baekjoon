{
  const N: string | null = prompt("줄을 선 사람의 수를 입력해주세요.");
  const n: number = N ? parseInt(N) : 0;
  if (n >= 1 && n <= 1000) {
    const t: string | null = prompt(
      "각 사람의 대기 시간을 빈칸을 두고 입력해주세요."
    );
    const waiting_time: Array<number> = t
      ? t.split(" ").map((v) => parseInt(v))
      : [];
    if (waiting_time.length === n) {
      waiting_time.sort();
      let ans = 0;
      waiting_time.forEach(
        (idx, n) =>
          (ans += waiting_time
            .slice(0, n + 1)
            .reduce((nxt, prv) => nxt + prv, 0))
      );
      console.log(ans);
    } else {
      console.log("대기 시간의 입력값 개수가 부적절합니다.");
    }
  } else {
    console.log("줄을 선 사람은 최소 1명에서 최대 1000명입니다.");
  }
}
/*
test

input
5
3 1 4 3 2

output
32

*/
