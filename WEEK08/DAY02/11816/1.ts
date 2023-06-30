{
  const error_msg = () => {
    console.log("부적절한 입력값입니다.");
  };
  const X: string | null = prompt(
    "8진수, 10진수, 또는 16진수에 해당되는 숫자를 "
  );
  if (X) {
    X.length >= 2 && X[0] === "0" && X[1] !== "x"
      ? console.log(parseInt(X, 8))
      : X.length >= 2 && X[0] === "0" && X[1] === "x"
      ? console.log(parseInt(X, 16))
      : console.log(X);
  } else {
    error_msg();
  }
}
