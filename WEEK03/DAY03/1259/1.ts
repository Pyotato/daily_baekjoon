{
  const error_msg = () => {
    console.log("입력값이 부적절합니다.");
  };
  while (true) {
    const num: string | null = prompt("숫자를 입력해주세요.");
    if (num) {
      if (parseInt(num) === 0) {
        break;
      }
      const temp: Array<string> = [];
      for (let i of num) {
        temp.push(i);
      }
      temp.reverse();
      const cmp: string = temp.join("");
      cmp == num ? console.log("yes") : console.log("no");
      continue;
    } else {
      error_msg();
      break;
    }
  }
}
