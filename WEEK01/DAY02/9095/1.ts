// https://www.acmicpc.net/problem/9095
const T: string | null = prompt("Enter number of test cases", "0");
const N: number | null = T ? parseInt(T) : null;
const test_cases: Array<number | null> = new Array(N);
if (N) {
  for (let i = 0; i < N; i++) {
    const t: string | null = prompt(`${i + 1}th case`);
    t ? (test_cases[i] = parseInt(t)) : null;
  }
}

const add123 = (n: number | null): number => {
  if (n) {
    return n === 1
      ? 1
      : n === 2
      ? 2
      : n === 3
      ? 4
      : add123(n - 1) + add123(n - 2) + add123(n - 3);
  } else {
    return -1;
  }
};

if (test_cases) {
  test_cases.map((v) => console.log(add123(v)));
}
//test
// 3
// 4
// 7
// 10
