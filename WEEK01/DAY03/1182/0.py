# https://www.acmicpc.net/problem/1182
# logic
# 부분 수열 -> 제시된 숫자들 부분적으로도 수열을 이루는 것 
# 등차 등비의 조건이 없을 때는 그냥 연속된 숫자들의 모임이라 생각하면 됨
# 0번째 인덱스부터 시작해 n-1번째 인덱스까지 각 원소의 값들을 넣고, 
# 해당 값을 지금까지 구해온 합에 더하는 경우와 더하지 않는 경우를 각 가지로 나누어 재귀함수를 호출한다.
# 각 재귀함수에서 지금까지의 합이 구하고자 하는 깂와 같다면 전역변수 cnt에 1을 더해주면 갯수를 세준다.
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
