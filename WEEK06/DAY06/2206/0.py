# 벽을 한개까지는 뿌실 수 있음

from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().strip().split())
g = [list(map(int, stdin.readline().strip())) for _ in range(N)] # 좌표 그래프 
v =[[[0]*2 for _ in range(M)] for _ in range(N)] # 방문 여부 표시 (벽)
d = [[-1,0],[1,0],[0,-1],[0,1]] #상하좌우 방향 표시

def bfs(x,y,wall,v,g):
    dq = deque()
    dq.append((x,y,wall))
    v[x][y][wall]=1 #방문(시작점)
    while dq:
        x,y,wall = dq.popleft()
        if x==N-1 and y==M-1: #도착점
            return v[x][y][wall]
        for i in d: #상하좌우 돌면서
            nx = x+i[0]
            ny = y+i[1]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if g[nx][ny]==0 and v[nx][ny][wall]==0: #벽 안뿌심
                dq.append((nx,ny,wall))
                v[nx][ny][wall]=v[x][y][wall]+1
            if g[nx][ny]==1 and wall==1: #벽 뿌심
                dq.append((nx,ny,wall-1))
                v[nx][ny][wall-1]=v[x][y][wall]+1
            print(v)
    return -1

print(bfs(0,0,1,v,g)) #x,y출발점, 뿌실 수 있는 벽 개수, 방문 여부, 좌표그래프