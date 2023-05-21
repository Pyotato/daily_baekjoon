{
  const N: string | null = prompt(
    "숫자 두개를 띄어쓰기로 구분해서 입력해주세요."
  );
  if (N) {
    const numbers: Array<number> = N.split(" ").map((v) => parseInt(v));
    if (numbers.length === 2) {
      //유클리드 호제법 :최대공약수 구하기
      const get_gcd = (n: Array<number>): number => {
        const a: number = n[0];
        const b: number = n[1];
        if (b == 0) {
          return a;
        }
        return get_gcd([b, a % b]);
      };
      //최소 공배수 구하기
      const get_lcm = (numbers: Array<number>, g: number) => {
        const mult: number = numbers.reduce((nxt, prv) => nxt * prv, 1);
        return mult / g;
      };
      const gcd: number = get_gcd(numbers);
      console.log(gcd);
      console.log(get_lcm(numbers, gcd));
    } else {
      console.log("입력값의 개수가 부족합니다.");
    }
  }
}
/*

input
24 18

output
6
72

*/
