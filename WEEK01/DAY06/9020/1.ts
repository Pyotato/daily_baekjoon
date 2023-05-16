{
  const t_count: string | null = prompt("테스트할 숫자의 개수를 입력해주세요.");
  const N: number = t_count ? parseInt(t_count) : 0;
  if (N > 0) {
    // const
  } else {
    console.log("테스트 케이스는 1개 이상 입력해주세요.");
  }
}
/*

* test
3
8
10
16 

output

3 5
5 5
5 11
*/
