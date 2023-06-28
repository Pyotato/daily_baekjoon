# https://www.acmicpc.net/problem/1149
# 이웃한 집과는 색이 다르면서
# 최소로 비용을 들여 색을 칠함
from sys import stdin
N = int(stdin.readline().strip()) #(2 ≤ N ≤ 1,000)
p = [list(map(int, stdin.readline().strip().split())) for _ in range(N)] #0 ==R, 1==G, 2 ==B
for i in range(1,len(p)):
    p[i][0]= min(p[i - 1][1], p[i - 1][2]) + p[i][0] #i번째 집을 R로 칠했을 때 최소
    p[i][1]= min(p[i - 1][0], p[i - 1][2]) + p[i][1] #i번째 집을 G로 칠했을 때 최소
    p[i][2]= min(p[i - 1][0], p[i - 1][1]) + p[i][2] #i번째 집을 B로 칠했을 때 최소
print(min(p[N-1][0],p[N-1][1],p[N-1][2])) # 칠한 집 중 가장 적은 비용 고르기
