{
  const error_msg = (inpt: string | null | number) => {
    const state = inpt ? inpt + "은" : inpt;
    console.log(`${state} 부적절한 입력값입니다.`);
  };
  const word: string | null = prompt(
    "문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같은 문자열을 입력해주세요."
  );
  const bomb: string | null = prompt(
    "1보다 크거나 같고, 36보다 작거나 같은 폭발 문자열을 입력해주세요."
  );
  if (word && bomb) {
    const ans: Array<string | null> = [];
    for (let i: number = 0; i < word.length; i++) {
      ans.push(word[i]);
      console.log(ans.slice(-bomb.length).join(""));
      if (ans.slice(-bomb.length).join("") === bomb) {
        for (let j = 0; j < bomb.length; j++) {
          ans.pop();
        }
      }
    }
    ans ? console.log(ans.join("")) : console.log("FRULA");
  } else {
    word && !bomb
      ? error_msg(bomb)
      : !word && bomb
      ? error_msg(word)
      : error_msg(`${word}와 ${bomb}은 `);
  }
}
