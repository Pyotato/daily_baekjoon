{
  const n: string | null = prompt("카드의 개수를 입력하세요.");
  const N: number = n ? parseInt(n) : 0;
  if (N >= 1 && N <= 500000) {
    let numbers: string | null = prompt(
      "카드에 있는 숫자들을 빈칸을 두고 입력해주세요."
    );

    const c: Array<string> = numbers ? numbers.split(" ") : [];
    if (c.length === N) {
      const m: string | null = prompt("갖고있는 카드의 개수를 입력하세요.");
      const M: number = m ? parseInt(m) : 0;
      if (M >= 1 && M <= 500000) {
        let cmds: string | null = prompt(
          "갖고 있는 지 구하려는 카드에 있는 숫자들을 빈칸을 두고 입력해주세요."
        );
        const num: Array<string> = cmds ? cmds.split(" ") : [];
        if (num.length === M) {
          const ans = new Map();
          c.map((v) =>
            !ans.get(v) ? ans.set(v, 1) : ans.set(v, ans.get(v) + 1)
          );
          console.log(ans);
          num.map((v) =>
            ans.get(v) ? console.log(ans.get(v)) : console.log(0)
          );
        } else {
          console.log(
            "갖고 있는지 구하려는 카드의 개수가 입력값과 불일치합니다."
          );
        }
      } else {
        console.log("구하려는 카드의 개수는 1 ≤ M ≤ 500,000개로 입력해주세요.");
      }
    } else {
      console.log("카드의 개수가 입력값과 불일치합니다.");
    }
  } else {
    console.log("카드의 개수는 1 ≤ N ≤ 500,000개로 입력해주세요.");
  }
}
/*
  * test
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
  
  * result
3 0 0 1 2 0 0 2
  
  */
