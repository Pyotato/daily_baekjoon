from sys import stdin
from collections import deque
n = int(stdin.readline().strip())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    p, c, w = map(int, stdin.readline().strip().split())
    tree[p].append((c, w))
    tree[c].append((p, w))
max_node = -1


def bfs(s):
    global max_node
    v = [-1]*(len(tree))
    dq = deque()
    dq.append([s, 0])
    v[s] = 0
    md = 0  # max distance
    while dq:
        n, d = dq.popleft()  # current node, distance
        for e, w in tree[n]:  # edge, weight
            if v[e] == -1:
                v[e] = 0
                dq.append([e, d+w])
                if md < d+w:
                    md = d+w
                    max_node = e
    return md


if n == 1:
    print(0)
else:
    bfs(1)
    print(bfs(max_node))
