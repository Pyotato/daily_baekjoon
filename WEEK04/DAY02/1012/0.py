# logic
# 전형적인 bfs
# 중첩배열에 배추의 위치를 1로 하여 for문을 돌면서 상하좌우에 1이 있다면 카운트를 해준다
# 조심할 포인트 : 가로와 세로 M과 N 임 주의 (idx out of range)

from collections import deque
T = int(input())

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def BFS(x, y):
    q = deque([(x, y)])
    f[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in d:
            nx, ny = x + i[0], y + i[1]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if f[nx][ny] == 1:
                q.append((nx, ny))
                f[nx][ny] = 0


for i in range(T):
    M, N, K = map(int, input().split())
    f = [[0]*(N) for _ in range(M)]
    cnt = 0

    for j in range(K):
        x, y = map(int, input().split())
        f[x][y] = 1

    for a in range(M):
        for b in range(N):
            if f[a][b] == 1:
                BFS(a, b)
                cnt += 1

    print(cnt)
