const N: string | null = prompt("직사각형의 가로 길이를 입력해주세요.");

if (N) {
  const n: number = parseInt(N);
  if (n >= 3 && n <= 1000) {
    const dp: Array<number> = [0, 1, 2];
    for (let i = 3; i < 1001; i++) {
      dp.push(dp[i - 2] + dp[i - 1]);
    }
    console.log(dp[n] % 10007);
  } else {
    console.log("직사각형의 가로 길이는 3이상 1000이하입니다.");
  }
} else {
  console.log("적절한 값을 입력해주세요.");
}
