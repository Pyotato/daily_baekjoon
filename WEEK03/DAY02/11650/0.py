# x, y 좌표 오름차순 정렬
from sys import stdin
N = int(stdin.readline())
points = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]
points.sort()
for i in points:
    print(i[0],i[1])

