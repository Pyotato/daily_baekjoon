from sys import stdin
#1 ≤ N ≤ 100,000,1 ≤ M ≤ 100,000,1 ≤ i ≤ j ≤ N
N, M = map(int, stdin.readline().strip().split())
nums = list(map(int, stdin.readline().strip().split()))
tests =[list(map(int, stdin.readline().strip().split())) for i in range(M)]
dp =[0 for _ in range(N+1)]
added =0

for i in range(N):
    added+=nums[i]
    dp[i+1]=added

for t in tests:
    s,e = t
    print(dp[e]-dp[s-1])