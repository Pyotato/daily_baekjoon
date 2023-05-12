# https://www.acmicpc.net/problem/13305
# logic
# 가능한 모든 케이스 구하기 (그리디) 
# 리터당 가격이 일정하다면 (배열에서 min값과 max값이 동일) forloop 거치지 않고 리턴 
# 최소가격은 for loop돌면서 현재가격과 지금까지 비교했던 값을 비교햇
# 작을 때만 업데이틓해준다.
# 리터 최소가격 * 거리를 합해 최소 비용을 구하기

from sys import stdin
N = int(stdin.readline().strip())
D = list(map(int, stdin.readline().strip().split())) # N-1
cost = list(map(int, stdin.readline().strip().split()))

def calc_cost(n:int,d:list,c:list):
    #가격이 모두 일정하다면 합 리턴
    if max(c)==min(c):
        return sum(d)
    cnt=0
    m_cost = c[0]
    for i in range(n-1):
        if c[i]<m_cost:
            m_cost=c[i]
        cnt +=m_cost*d[i]
    return cnt
print(calc_cost(N,D,cost))
# test1
# 4
# 2 3 1
# 5 2 4 1

# test2
# 4
# 3 3 4
# 1 1 1 1