const test1 = 10;
const test2 = 123114;
const test3 = 121;
const test4 = 5;
const convert_to_one = (n: number) => {
  const arr: Array<number> = new Array(n + 1);
  arr.fill(0);

  arr.map((item, idx) => {
    if (idx >= 2) {
      arr[idx] = arr[idx - 1] + 1;
      if (idx % 3 === 0) {
        arr[idx] = Math.min(arr[idx], arr[idx / 3] + 1);
      }
      if (idx % 2 === 0) {
        arr[idx] = Math.min(arr[idx], arr[idx / 2] + 1);
      }
    }
  });
  return arr[n];
};
console.log(convert_to_one(test1));
console.log(convert_to_one(test2));
console.log(convert_to_one(test3));
console.log(convert_to_one(test4));
