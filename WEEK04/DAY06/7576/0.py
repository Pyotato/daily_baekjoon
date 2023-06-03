# logic
# bfs
# 칸을 이동하면서 방문한다고 했을 때 
# 인접한 거를 모두 1로 바꾸고 익은 토마토의 좌표들을 덱에 넣기
# 방문하면서 1씩 카운트
# 모두 방문 시 0인 게 남아있다면 -1리턴
from sys import stdin
from collections import deque
input = stdin.readline().strip()
M,N = map(int, input.split())
dir_ = [[-1, 0], [1, 0], [0, -1], [0, 1]]
t = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
    
cnt=0

q = deque([])
for i in range(N):
    for j in range(M):
        if t[i][j]==1:
            q.append([i,j])

def bfs():
    while q:
        x,y = q.popleft()
        for d in dir_:
            nx,ny = x+d[0],y+d[1]
            if 0<=nx<N and 0<=ny<M and t[nx][ny]==0:
                t[nx][ny]=t[x][y]+1
                q.append([nx,ny])

def tomato(cnt):
    bfs()
    for i in t:
        for j in i:
            if j==0:
                return -1
        cnt = max(cnt, max(i))   
    return cnt-1
print(tomato(cnt))