{
  const error_msg = (inpt: string | null) => {
    console.log(`${inpt}은 부적절한 입력값입니다.`);
  };
  const input_err = (inpt: number, len: number) => {
    let state: string = inpt < len ? "부족합" : "너무 많습";
    console.log(
      `입력값의 개수가 ${state}니다.입력한 값의 개수 :${inpt}, 입력해야하는 값의 개수 :${len} `
    );
  };
  const input1: string | null = prompt(
    "집합A와 B의 길이를 각각 공백을 두고 입력해주세요."
  );
  if (input1) {
    const [A_length, B_length]: Array<number> = input1
      .split(" ")
      .map((v) => parseInt(v));
    const [input2, input3]: Array<string | null> = [
      prompt("집합A의 원소를 띄어쓰기로 구분해서 입력해주세요."),
      prompt("집합B의 원소를 띄어쓰기로 구분해서 입력해주세요."),
    ];
    if (input2 && input3) {
      const A = new Array(...input2.split(" "));
      const B = new Array(...input3.split(" "));
      if (A_length !== A.length || B_length !== B.length) {
        A_length !== A.length
          ? input_err(A.length, A_length)
          : input_err(B.length, B_length);
      } else {
        const [a, b] = [
          A.filter((v) => B.includes(v)),
          B.filter((v) => A.includes(v)),
        ];
        console.log(a.length + b.length);
      }
    } else {
      input2 ? error_msg(input3) : error_msg(input2);
    }
  } else {
    error_msg(input1);
  }
}
