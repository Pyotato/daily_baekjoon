import sys
input = sys.stdin.readline


def solution():
    n = int(input())

    # Initialize dp arrays
    dp = [0] * (n+1)
    dp_2 = [0] * (n+1)

    # Calculate dp array
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    now_idx = 2
    while dp[now_idx] <= n:
        now_idx += 1
        dp[now_idx] = dp[now_idx-1] + dp[now_idx-2]

    # Calculate dp_2 array
    min_output = 0
    max_output = 0
    tmp_c = n
    if tmp_c % 2 == 1:
        tmp_c -= 3
        min_output += 2
    min_output += tmp_c // 2
    tmp_c = n
    dp_2[2] = 1
    dp_2[3] = 2
    dp_2[4] = 2
    dp_2[5] = 3
    dp_2[6] = 4
    for i in range(7, n+1):
        now_max = -1
        tmp_idx = 2
        while dp[tmp_idx] <= i:
            now_max = max(now_max, dp_2[dp[tmp_idx]] + dp_2[i - dp[tmp_idx]])
            tmp_idx += 1
        dp_2[i] = now_max
    max_output=dp_2[n]
    print(min_output, max_output)


solution()
