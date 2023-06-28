# from sys import stdin
# N, M = map(int, (stdin.readline().strip().split()))
# g = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
# for _ in range(M):
#     ans = 0
#     x1, y1, x2, y2 = map(int, (input().split()))
#     for i in range(x1-1, x2):
#         for j in range(y1-1, y2):
#             ans += g[i][j]
#     print(ans)

# 시간초과..dp로 풀자

from sys import stdin
N, M = map(int, (stdin.readline().strip().split()))
g = [list(map(int, stdin.readline().strip().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+g[i-1][j-1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, (stdin.readline().strip().split()))
    print(dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])
