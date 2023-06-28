# 다익스트라 문제 연습
from sys import stdin,maxsize
from heapq import heappush, heappop
V,E = map(int, stdin.readline().strip().split())
inf = maxsize
S = int(stdin.readline().strip())
dp = [inf]*(V+1) #방문여부
heap = []
g = [[] for _ in range(V+1)]

def dijkstra(s):
    for _ in range(E): #노드 그래프 초기화
        u,v,w = map(int,stdin.readline().strip().split())
        g[u].append((w,v)) #가중치, 목적지 노드
    
    dp[s]=0 #시작점은 0으로
    heappush(heap,(0,s)) #시작점 heap넣기
    
    while heap:
        c,n = heappop(heap)

        if dp[n] < c: #가중치 크면 업데이트 x
            continue

        for acc_w , nxt in g[n]:
            nxt_w = acc_w + c
            if nxt_w < dp[nxt]:
                dp[nxt] = nxt_w
                heappush(heap , (nxt_w , nxt))

    for i in range(1,V+1):
         print("INF") if dp[i]==inf else print(dp[i])

dijkstra(S)
