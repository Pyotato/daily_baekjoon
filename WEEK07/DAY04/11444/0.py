# 피보나치 수 6
# Fn = Fn-1 + Fn-2 (n ≥ 2)
# n<=1,000,000,000,000,000,000
# n번째 피보나치 수를 1,000,000,007으로 나눈 나머지

# 피보나치 문제풀이들 참고 : https://www.acmicpc.net/blog/view/28

# N 제한은 10^18 이지만, 1,000,000,007로 나눈 나머지를 구해야 함
# 너무 큰 n... 해당 문제는 행렬로 풀어야함
from sys import stdin
n = int(stdin.readline().strip())
div = 1000000007
#초기 행렬
adj=[[1,1],[1,0]]
#피보나치 초기값
start=[[1],[1]]
#제곱을 구하는 분할정복
def power(adj,n):
    if n==1: 
        return adj
    elif n%2: 
        return multi(power(adj,n-1),adj)
    else:
        return power(multi(adj,adj),n//2)
#행렬의 곱셈
def multi(a,b):
    temp=[[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum=0
            for k in range(2):
                sum+=a[i][k]*b[k][j]
            temp[i][j]=sum%div
            # print(temp)
    return temp
if n<3:
    print(1)
else:
    print(multi(power(adj,n-2),start)[0][0])
    
