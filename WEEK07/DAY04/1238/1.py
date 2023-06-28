from sys import stdin, maxsize
from heapq import heappush, heappop
N, M, X = map(int, stdin.readline().strip().split())
inf = maxsize
g = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, stdin.readline().strip().split())
    g[u].append((w, v))
ans = [0 for _ in range(N)] 
def dijkstra(n,otw_back):
    heap = []
    dp = [inf]*(N+1)
    start = n if otw_back else X
    dp[start] =0
    heappush(heap,(0,start))
    while heap:
        cost,nxt = heappop(heap)
        if dp[nxt]<cost: # 최소값일 때만 업데이트
            continue
        for acc_cost , idx in g[nxt]:
            nxt_cost = acc_cost+cost
            if nxt_cost < dp[idx]:
                dp[idx]=nxt_cost
                heappush(heap,(nxt_cost,idx))
    return (dp[n],dp[X])

for n in range(1,N+1):
    a = dijkstra(n,False)
    b = dijkstra(n,True)
    ans.append((sum([list(a)[0],list(b)[-1]])))

print(max(ans))