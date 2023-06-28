#1932랑 비슷한 문제

# 스티커가 다음과 같다고 치면 
# |c1|c2|c3| c4|c5|
# |--|--|--|--|--|
# |50 |10 |100| 20| 40|
# |30 |50 |70 |10| 60|

# c1에서는 하나만 선택가능하고 c2에서는 그 선택한 스티커의 대각선밖에 선택이 가능합니다.
# 따라서 c2부터 이전 c의 대각선에 있는 값 중 가장 큰 값을 현제의 cell에 넣어줘서
# 마지막 column중 큰 cell을 출력합니다.

import sys
input = sys.stdin.readline
T = int(input().rstrip())
ans = []
for _ in range(T):
    N = int(input())    #(1 ≤ n ≤ 100,000)
    stk = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1,N):
        if i == 1:
            stk[0][i] += stk[1][i-1]
            stk[1][i] += stk[0][i-1]
        else:
            stk[0][i] += max(stk[1][i-1],stk[1][i-2])
            stk[1][i] += max(stk[0][i-1],stk[0][i-2])

    print(max(stk[0][N-1],stk[1][N-1]))