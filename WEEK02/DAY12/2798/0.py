# https://www.acmicpc.net/problem/2609
# logic
# 조합(combinations) 활용
# 3개 조합해서 더한값들을 배열에 담아서
# 합이 최대면서 구하려는 숫자보다 작은 경우 반환


from sys import stdin
from itertools import combinations
N, M = map(int, stdin.readline().strip().split())
cards = list(map(int, stdin.readline().strip().split()))

def blackjack(m: int, c: list) -> int:
    c = list(map(sum, combinations(c, 3)))
    ans = 0
    for i in c:
        if i <= m and ans < i:
            ans = i
    return ans

print(blackjack(M, cards))
