{
  const nm: string | null = prompt("카드의 개수 N과 목표 수 M를 입력해주세요.");
  const N: number = nm ? nm.split(" ").map((v) => parseInt(v))[0] : 0;
  const M: number = nm ? nm.split(" ").map((v) => parseInt(v))[1] : 0;
  if (N > 0) {
    if (M >= 10 && M <= 300000) {
      const card_input: string | null = prompt(
        "카드 수들을 공백을 두고 입력해주세요."
      );
      const card: Array<number> = card_input
        ? card_input.split(" ").map((v) => parseInt(v))
        : [];
      if (card.length === N) {
        if (card.length >= 3 && card.length <= 100) {
          const blackjack = (card: Array<number>, M: number) => {
            let ans: number = 0;
            for (let i = 0; i < card.length; i++) {
              for (let j = i + 1; j < card.length; j++) {
                for (let k = j + 1; k < card.length; k++) {
                  card[i] + card[j] + card[k] > ans &&
                  card[i] + card[j] + card[k] <= M
                    ? (ans = card[i] + card[j] + card[k])
                    : ans;
                }
              }
            }
            return ans;
          };
          console.log(blackjack(card, M));
        } else {
          console.log("카드에 적힌 수가 부적절합니다.");
        }
      } else {
        console.log("카드의 개수가 부적절합니다.");
      }
    } else {
      console.log("카드의 숫자는 10이상 300000으로 입력해주세요.");
    }
  } else {
    console.log("카드의 개수는 1개 이상 입력해주세요.");
  }
}
/*
* test 1 
input
5 21
5 6 7 8 9

output
21

* test 2
10 500
93 181 245 214 315 36 185 138 216 295

output
497
*/
