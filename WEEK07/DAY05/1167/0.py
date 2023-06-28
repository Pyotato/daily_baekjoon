#두 점 사이의 거리 중 가장 긴 것
from sys import stdin
from collections import deque
V = int(stdin.readline().strip()) #2 ≤ V ≤ 100,000
tree = [[] for _ in range(V + 1)]
for _ in range(V):
    t = list(map(int, stdin.readline().strip().split()))
    for e in range(1, len(t) - 2, 2):
        tree[t[0]].append((t[e + 1],t[e])) # w,e

def bfs(s):
    visited = [-1]*(V+1)
    dq = deque()
    dq.append(s)
    visited[s]=0
    ans = [0,0]
    while dq:
        b = dq.popleft()
        for w,e in tree[b]:
            if visited[e] == -1:
                visited[e] = visited[b]+w
                dq.append(e)
                if ans[0] < visited[e]:
                    ans = visited[e],e
    return ans

d, node = bfs(1) #노드 1부터 시작
d, node = bfs(node) 
print(d)
