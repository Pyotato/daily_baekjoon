#양끝까지 자식 branch 합 더해줘서 내려오기
from sys import stdin
n = int(stdin.readline().strip())
t = [list(map(int, stdin.readline().strip().split()))for _ in range(n)]
cnt = 2 #밑의 가지들만 더해줌
for i in range(1, n):
    for j in range(cnt):
        if j == 0:
            t[i][j] = t[i][j]+t[i-1][j]
        elif j == i:
            t[i][j] = t[i][j]+t[i-1][j-1]
        else: #양끝 제외 더해주는 경우: 제일 큰 값으로 채우기
            t[i][j] = max(t[i-1][j], t[i-1][j-1]) + t[i][j]
    cnt += 1
print(max(t[n-1]))
