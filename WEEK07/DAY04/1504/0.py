# a와 b 사이의 양방향 길,
# 다시 갈 수는 있지만 꼭 건너야하는 지점은 거치고
# 최소 경로로 가야함
from sys import stdin,maxsize
from heapq import heappop, heappush
N, E = map(int, stdin.readline().strip().split())
inf =maxsize
g = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int, stdin.readline().strip().split())
    g[a].append((c,b))
    g[b].append((c,a))
v1,v2 = map(int, stdin.readline().strip().split())

def dijkstra(n):
    heap = []
    dp =[inf]*(N+1)
    dp[n]=0
    heappush(heap,(0,n))
    while heap:
        cst, nxt = heappop(heap)
        if dp[nxt]<cst:
            continue
        for acc_c , idx in g[nxt]:
            nxt_c = acc_c+cst
            if nxt_c < dp[idx]:
                dp[idx] = nxt_c
                heappush(heap,(nxt_c,idx))
    return dp

s1 = dijkstra(1) #start 1
sv1 = dijkstra(v1) #start v1
sv2 = dijkstra(v2) #start v2

v1_route = s1[v1]+sv1[v2]+sv2[N]
v2_route = s1[v2]+sv1[N]+sv2[v1]

ans = min(v1_route,v2_route)
print(ans if ans<inf else -1) 