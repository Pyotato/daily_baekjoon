from heapq import heappush, heappop
from sys import stdin
N = int(stdin.readline().strip())
hq = []
for _ in range(N):
    cmd = int(stdin.readline().strip())
    if cmd == 0:
        print(0) if len(hq) == 0 else print(heappop(hq))
    else:
        heappush(hq, cmd)
