# https://www.acmicpc.net/problem/2468
# logic
# NxN크기의 영역에서 물의 높이는 0이상이다.
# 영역에서 지역의 높이는 2이상 100이하이다.
# 물에 잠기지 않는 "지역" 은
# 지역의 높이 > 물의 높이인 곳
# 물에 잠기지 않는 "영역" 은
# 상하좌우가 인접한 경우 하나로 친다.
# bfs로 방문여부(0==방문X,1==방문)와 잠김여부 (0==잠김,1==안잠김)로
# 방문하지 않았으면서 잠기지 않는 영역의 개수를 세준다.
# 방문 개수를 세줄 때 deque에 넣어 모두 방문할때까지 popleft를 해주기
# 모든 물의 높이를 고려할 필요가 없으므로 최고 물 높이를 입력값을 받아올 때 구한다.
# 최고 물 높이는 가장 높은 지역의 높이 -1이다. (같으면 모든 지역이 잠기므로)
from sys import stdin
import sys
sys.setrecursionlimit(10*6)
from collections import deque

N = int(stdin.readline().strip())
area = []
max_a = 1
d=[[0,1],[0,-1],[1,0],[-1,0]]
for _ in range(N):
    l = list(map(int, stdin.readline().strip().split()))
    max_a = max(l) if max_a < max(l) else max_a
    area.append(l)
cnt=0

def bfs(i,j,fld,visited):
    q = deque()
    q.append((i,j))
    visited[i][j]=1
    while q: 
        x,y = q.popleft()
        for k in range(4):
            nx = x + d[k][0]
            ny = y + d[k][1]
            if 0 <= nx < N and 0 <= ny < N:
                if fld[nx][ny] ==1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1 
                    q.append((nx, ny))

def sunk(a, max_a):
    h = max_a-1
    fld = [[0]*N for _ in range(N)]
    safe_max=[]

    while h >= 0: #1로 해줬을때 런타임에러..물높이가 0일 수도 있음!
        for x in range(N):
            for y in range(N):
                if a[x][y] > h: #잠김 = 0, 잠기지 않음 =1
                    fld[x][y] = 1
        h -= 1
        visited = [[0] * N for _ in range(N)]
        cnt=0
        for i in range(N):
            for j in range(N):
                if fld[i][j]==1 and visited[i][j]==0:
                    bfs(i,j,fld,visited) #메모리가 재귀 쓸떄 나았음
                    cnt+=1
        safe_max.append(cnt)
    return max(safe_max)


print(sunk(area, max_a))


# # test
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
# ans=5

# test
# 7
# 9 9 9 9 9 9 9
# 9 2 1 2 1 2 9
# 9 1 8 7 8 1 9
# 9 2 7 9 7 2 9
# 9 1 8 7 8 1 9
# 9 2 1 2 1 2 9
# 9 9 9 9 9 9 9
# ans=6
