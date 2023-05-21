{
  const n: string | null = prompt("설탕의 무게를 입력해주세요.");
  const N: number = n ? parseInt(n) : 0;
  if (N >= 3 && N <= 5000) {
    let cnt: number = 0;
    const deliver = (N: number): number => {
      while (N >= 0) {
        if (N % 5 === 0) {
          console.log("N", N);
          cnt += N / 5;
          return cnt;
        }
        console.log("N", N);
        N -= 3;
        cnt += 1;
      }

      return -1;
    };

    N === 3 || N === 5 ? console.log(1) : console.log(deliver(N));
  } else {
    console.log("설탕 무게 입력값이 부적절합니다.");
  }
}
/**
 * test1
 * input
   18
 * output
   4
 * 
 * test2
 * input
   4
 * output
   -1
 * * test3
 * input
   6
 * output
   2
 * * test4
 * input
   9
 * output
   3
 * * test5
 * input
   11
 * output
   3
 * 
 */
