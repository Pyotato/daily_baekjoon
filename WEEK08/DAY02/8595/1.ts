{
  const error_msg = (input: string | null) => {
    input
      ? console.log(`${input}은 부적절한 입력값입니다.`)
      : console.log("값을 입력해주세요.");
  };
  const n: string | null = prompt(
    "1 ≤ n ≤ 5,000,000인 단어 길이 n을 입력해주세요."
  );
  const nums: Array<number> = new Array(9).fill(0);
  nums.map((idx, v) => (nums[idx + 1] = idx + 1)); //[0,1,2,3,4,5,6,7,8,9]
  if (n) {
    const word: string | null = prompt(`길이가 ${n}인 단어를 입력해주세요.`);
    if (word) {
      if (word.length === parseInt(n)) {
        let [place_value, ans, temp]: Array<number> = [1, 0, 0];
        for (let i = parseInt(n) - 1; i >= 0; i--) {
          //배열 뒤에서부터 item 확인
          // console.log(word[i]);
          if (nums.includes(parseInt(word[i]))) {
            temp += parseInt(word[i]) * place_value;
            place_value = place_value * 10;
          }
          if (i === 0 || !nums.includes(parseInt(word[i]))) {
            //맨앞에서부터 숫자가 시작하거나 숫자가 아닌 경우
            if (place_value >= Math.pow(10, 7)) {
              place_value = 1;
              temp = 0;
              continue;
            }
            ans += temp;
            place_value = 1;
            temp = 0;
          }
        }
        console.log(ans);
      } else {
        error_msg(word);
      }
    } else {
      error_msg(word);
    }
  } else {
    error_msg(n);
  }
}
