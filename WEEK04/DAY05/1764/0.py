from sys import stdin
input = stdin.readline().strip()
N, M = map(int, input.split())
notheard, notseen = set(), set()

for _ in range(N):
    notheard.add(stdin.readline().strip())

for _ in range(M):
    notseen.add(stdin.readline().strip())
ans = list(notheard.intersection(notseen))
ans.sort()
print(len(ans))
print("\n".join(ans))
