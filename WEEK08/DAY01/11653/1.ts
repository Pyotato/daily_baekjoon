{
  const error_msg = () => {
    console.log("입력값이 부적절합니다.");
  };
  const N: string | null = prompt(
    "1보다 크거나 같고 10,000,000보다 작거나 같은 값을 입력해주세요."
  );
  if (N) {
    let n: number = typeof parseInt(N) === "number" ? parseInt(N) : -1;
    if (n) {
      if (n > 1 && n <= 3) console.log(n);
      else {
        let i: number = 2;
        // console.log(n);
        while (n !== 1) {
          if (n % i === 0) {
            n /= i;
            console.log(i);
          } else {
            i++;
          }
        }
      }
    } else {
      error_msg();
    }
  } else {
    error_msg();
  }
}
