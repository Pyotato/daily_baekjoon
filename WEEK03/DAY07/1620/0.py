# https://www.acmicpc.net/problem/1620
#logic
# p1은 번호를 키로 하여 바로 dict에 접근하도록,
# p2는 포켓몬 이름을 키로 하여 바로 접근하도록 풀이
# 단, 번호는 1번부터 시작하며 
# 시험문제가 번호로 주어졌을때는 p1에 접근, 이름으로 주어졌을때는 p2에 접근하도록 하기


import sys
input = sys.stdin.readline
N, M = map(int, input().split())  # 1<=N,M<=100000
p1, p2 = dict(), dict()
for i in range(1, N + 1):
    pkm = input().rstrip()
    p1[str(i)] = pkm
    p2[pkm] = str(i)

for _ in range(M):
    q = input().rstrip()
    print(p1[q]) if q.isdigit() else print(p2[q])
