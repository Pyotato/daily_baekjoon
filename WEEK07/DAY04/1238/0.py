from sys import stdin, maxsize
from heapq import heappush, heappop
N, M, X = map(int, stdin.readline().strip().split())
inf = maxsize
g = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, stdin.readline().strip().split())
    g[u].append((w, v))
ans = []

def dijkstra(n):
    heap = []
    dp = [inf]*(N+1)
    dp[n] = 0 #시작점
    heappush(heap,(0,n))
    while heap:
        cost,nxt = heappop(heap)
        if dp[nxt]<cost: # 최소값일 때만 업데이트
            continue
        for acc_cost , idx in g[nxt]:
            nxt_cost = acc_cost+cost
            if nxt_cost < dp[idx]:
                dp[idx]=nxt_cost
                heappush(heap,(nxt_cost,idx))
    # 돌아오는 길
    dp2 = [inf]*(N+1)
    dp2[X] = 0 #시작점
    heappush(heap,(0,X))
    while heap:
        cost,nxt = heappop(heap)
        if dp2[nxt]<cost: # 최소값일 때만 업데이트
            continue
        for acc_cost , idx in g[nxt]:
            nxt_cost = acc_cost+cost
            if nxt_cost < dp2[idx]:
                dp2[idx]=nxt_cost
                heappush(heap,(nxt_cost,idx))
    ans.append(dp[X]+dp2[n])

for n in range(1,N+1):
    dijkstra(n)
print(max(ans))