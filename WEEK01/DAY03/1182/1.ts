const N_S: string | null = prompt("enter number of cases and target number:");
if (N_S) {
  const N: number = parseInt(N_S.split(" ")[0]);
  const S: number = parseInt(N_S.split(" ")[1]);
  const test_str: string | null = prompt("Enter sequence:");
  const t: Array<number> | null = test_str
    ? test_str.split(" ").map((v: string) => parseInt(v))
    : [];
  let count: number = 0;

  if (N === t.length) {
    const dfs = (n: number, s: number) => {
      if (n >= N) {
        return count;
      }
      s += t[n];
      if (s === S) {
        count++;
      }
      dfs(n + 1, s);
      dfs(n + 1, s - t[n]);
      return count;
    };

    console.log(dfs(0, 0));
  } else {
    console.log("invalid number of args");
  }
} else {
  console.log("invalid args");
}

// test
// 5 0
// -7 -3 -2 5 8
