# 1 ≤ M ≤ N ≤ 8
# 1 ~ N 자연수 중에서 중복없이 M개를 고른 수열
import sys
from itertools import combinations
input = sys.stdin.readline().rstrip()
N,M = map(int,input.split())
if N ==M :
    print(" ".join(list(map(lambda i: str(i+1), range(N)))))
else:
    cmb = list(combinations(range(1,N+1),M))
    cmb.sort()
    for i in cmb:
        for j in range(len(i)):
            print(i[j], end=" ")
        print()