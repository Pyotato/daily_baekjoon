from sys import stdin
A, B = map(int, stdin.readline().strip().split())
set_A = set(map(int, stdin.readline().strip().split()))
set_B = set(map(int, stdin.readline().strip().split()))
print(len(set_A.difference(set_B))+len(set_B.difference(set_A)))
