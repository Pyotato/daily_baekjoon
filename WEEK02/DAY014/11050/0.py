# https://www.acmicpc.net/problem/11050
# logic
# 이항계수
# 조합의 개수 구하기
# 5C2 => 10

from sys import stdin
from itertools import combinations
N, M = map(int, stdin.readline().strip().split())

print(len(list(combinations(range(N),M))))

# input
# 5 2
# 10