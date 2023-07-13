from itertools import combinations
from sys import stdin

n, k = map(int, input().split())
answer = 0

first_word = {'a', 'n', 't', 'i', 'c'}

remain_alphabet = set(chr(i) for i in range(97, 123)) - first_word

data = [stdin.readline().rstrip()[4:-4] for _ in range(n)]


def learn(data, learned):
    cnt = 0
    for word in data:
        canRead = 1
        for w in word:
            # 안배웠으니까 못읽는다.
            if learned[ord(w)] == 0:
                canRead = 0
                break
        if canRead == 1:
            cnt += 1
    return cnt


if k >= 5:
    learned = [0] * 123
    for x in first_word:
        learned[ord(x)] = 1

    # 남은 알파벳 중에서 k-5개를 선택해본다.
    for teach in list(combinations(remain_alphabet, k-5)):
        for t in teach:
            learned[ord(t)] = 1
        cnt = learn(data, learned)

        if cnt > answer:
            answer = cnt
        for t in teach:
            learned[ord(t)] = 0
    print(answer)
else:
    print(0)
