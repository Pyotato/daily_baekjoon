const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString();
input = input.split("\n");
// const n = prompt("1 ≤ n ≤ 5,000,000인 단어 길이 n을 입력해주세요.");
const nums = new Array(9).fill(0);
nums.map((idx, v) => (nums[idx + 1] = idx + 1)); //[0,1,2,3,4,5,6,7,8,9]
// const word = prompt(`길이가 ${n}인 단어를 입력해주세요.`);
let [place_value, ans, temp] = [1, 0, 0];
for (let i = parseInt(n) - 1; i >= 0; i--) {
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
