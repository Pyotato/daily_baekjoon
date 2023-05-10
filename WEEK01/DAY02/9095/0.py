# https://www.acmicpc.net/problem/9095
from sys import stdin
T = int(stdin.readline().strip())
t = list(map(lambda _: int(stdin.readline().strip()), range(T)))
# 1일 경우 1가지
# 2일 경우 1+1 , 2로 두가지
# 3일 경우 1+1+1, 2+1, 1+2, 3으로 4가지
# 4일 경우 4+2+1 즉 n-1 n-2 n-3으로 재귀

def add123(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return add123(n-1)+add123(n-2)+add123(n-3)


for i in t:
    print(add123(i))
