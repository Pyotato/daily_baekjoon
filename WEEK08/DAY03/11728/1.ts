{
  const error_msg = (inpt: string | null | number) => {
    const state = inpt ? inpt + "은" : inpt;
    console.log(`${state} 부적절한 입력값입니다.`);
  };
  const inpt: string | null = prompt(
    "배열 A와 B의 길이를 공백을 두고 입력해주세요."
  );
  if (inpt) {
    const [N, M] = inpt.split(" ").map((v) => parseInt(v));
    const [A, B]: Array<string | null> = [
      prompt("배열 A와 B의 길이를 공백을 두고 입력해주세요."),
      prompt("배열 A와 B의 길이를 공백을 두고 입력해주세요."),
    ];
    if (A && B) {
      const a: Array<number> = A.split(" ").map((v) => parseInt(v));
      const b: Array<number> = B.split(" ").map((v) => parseInt(v));
      if (a.length === N && b.length === M) {
        const M: Array<number> = [...a, ...b];
        M.sort();
        console.log(M.join(" "));
      }
    } else {
      B ? error_msg(A) : error_msg(B);
    }
  } else {
    error_msg(inpt);
  }
}
