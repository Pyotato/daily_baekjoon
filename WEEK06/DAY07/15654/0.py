from sys import stdin
from itertools import permutations
N, M = map(int, stdin.readline().strip().split()) #1 ≤ M ≤ N ≤ 8
nums = list(map(int,stdin.readline().strip().split()))
nums.sort()
cmb = list(permutations(nums,M))
for i in range(len(cmb)):
    print(" ".join(list(map(lambda j: str(j),cmb[i]))))