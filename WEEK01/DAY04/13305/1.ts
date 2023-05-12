const input: string | null = prompt(
  "도시의 개수 N을 입력해주세요 (2<N<=100000)"
);
const distance: string | null = prompt("도시 간의 거리를 입력해주세요.");
const cost: string | null = prompt(
  "도시 간의 주유소 리터당 가격을 입력해주세요."
);

const N: number = input ? parseInt(input) : 0;
const dist: Array<number> = distance
  ? distance.split(" ").map((v) => parseInt(v))
  : [];
const cst: Array<number> = cost ? cost.split(" ").map((v) => parseInt(v)) : [];

const calc_cost = (n: number, d: Array<number>, c: Array<number>): number => {
  if (Math.max(...d) === Math.min(...d)) {
    return d.reduce((nex, prv) => nex + prv, 0);
  } else {
    let cnt = 0;
    let min_cost = c[0];
    for (let i = 0; i < n - 1; i++) {
      if (c[i] < min_cost) {
        min_cost = c[i];
      }
      cnt += min_cost * d[i];
    }
    return cnt;
  }
};
N < 2
  ? console.log("도시는 2개 이상 입력해주세요.")
  : dist.length !== N - 1
  ? console.log("도시 간의 거리 개수가 불일치 합니다.")
  : cst.length === N
  ? console.log(calc_cost(N, dist, cst))
  : console.log("도시의 개수가 불일치 합니다.");

/*
test1
4
2 3 1
5 2 4 1

test2
4
3 3 4
1 1 1 1

*/
