from sys import stdin
N, M = map(int, stdin.readline().strip().split())
A, B = list(map(int, stdin.readline().strip().split())), list(
    map(int, stdin.readline().strip().split()))
M = [*A, *B]
M.sort()
print(*M)
