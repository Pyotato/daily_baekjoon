# https://www.acmicpc.net/problem/1182
from sys import stdin

N, S = map(int, stdin.readline().strip().split())
d = list(map(int, stdin.readline().strip().split()))
cnt = 0


def dfs(n: int, s: int) -> int:
    global cnt
    if n >= N:
        return cnt
    s += d[n]
    if s == S:
        cnt += 1
    dfs(n+1, s)
    dfs(n+1, s-d[n])
    return cnt


print(dfs(0, 0))
