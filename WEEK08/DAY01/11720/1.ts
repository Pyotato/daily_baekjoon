{
  const error_msg = () => {
    console.log("입력값이 부적절합니다.");
  };
  const N: string | null = prompt(
    "1보다 크거나 같고 100보다 작거나 같은 값을 입력해주세요."
  );
  const nums: string | null = prompt(`${N}개의 숫자를 공백없이 입력해주세요.`);
  if (N) {
    let n: number = typeof parseInt(N) === "number" ? parseInt(N) : -1;
    let num_arr: Array<number> | null = nums
      ? [...nums].map((v) => parseInt(v))
      : null;
    if (n && num_arr) {
      console.log(num_arr.reduce((prv, nxt) => prv + nxt, 0));
    } else {
      error_msg();
    }
  } else {
    error_msg();
  }
}
