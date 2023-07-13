import { error_msg, Inputs } from "../../../errormsg";
{
  const inpt: Inputs["err"] | Inputs["N"] = prompt(
    "자연수 N(1 ≤ N ≤ 1,000,000)를 입력해주세요."
  );

  if (inpt && typeof parseInt(inpt) === "number") {
    const n = parseInt(inpt);
    for (let i = 1; i < n + 1; i++) {
      const num = i.toString();
      const temp = new Array().fill(num);
    }
  } else {
    error_msg(inpt);
  }
}
