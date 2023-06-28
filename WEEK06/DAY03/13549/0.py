# 다익스트라 문제
# 준비물 : node담을 list, 방문여부 저장할 dp테이블, 최소비용으로 정렬해줄 heap

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

n, k = map(int, input().split())
dp = [inf] * (100001)
heap = []


def dijkstra(n, k):
    if k <= n: #동생의 위치가 수빈의 위치보다 뒤라면 수빈이는 -1씩 뒤로 가서 찾는 조건 밖에 없음
        print(n - k)
        return

    heappush(heap, [0, n]) #출발 node 힙에 넣기
    while heap:
        w, n = heappop(heap)
        for nx in [n + 1, n - 1, n * 2]: #1칸앞으로 , 1칸 뒤로, 순간이동
            if 0 <= nx <= 100000:
                if nx == n * 2 and dp[nx] == inf: #순간이동을 할 거고 방문하지 않았으면
                    dp[nx] = w
                    heappush(heap, [w, nx])
                elif dp[nx] == inf: # 그외에 1씩 앞으로 가줘야할 때 (방문 X)
                    dp[nx] = w + 1
                    heappush(heap, [w + 1, nx])
    print(dp)
    print(dp[k])


dijkstra(n, k)
