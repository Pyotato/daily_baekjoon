{
  class Comb {
    select_n: number; //조합 시 고를 숫자 개수
    arr: Array<unknown>; //조합을 찾을 배열
    combination: Set<unknown>; //
    constructor() {
      this.select_n = 0;
      this.arr = [];
      this.combination = new Set();
    }
    //조합 구해서 리턴해주기
    get_comb(n: Comb["select_n"], arr: Comb["arr"]) {}
  }
  const c = new Comb();
}
