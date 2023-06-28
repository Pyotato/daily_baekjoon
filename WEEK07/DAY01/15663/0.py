from itertools import permutations
from sys import stdin #(1 ≤ M ≤ N ≤ 8)
N,M = map(int,stdin.readline().strip().split())
nums = list(map(int,stdin.readline().strip().split()))
nums.sort()
prm = list(set(permutations(nums,M)))
prm.sort()
for i in prm:
    print(" ".join(map(str,i)))