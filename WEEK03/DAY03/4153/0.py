# https://www.acmicpc.net/problem/4153

from sys import stdin
while True:
    t = list(map(int, stdin.readline().strip().split()))
    t.sort()
    a, b, c = t[0], t[1], t[2]
    if a == 0 and b == 0 and c == 0:
        break

    print("right") if pow(a, 2)+pow(b, 2) == pow(c, 2) else print("wrong")
