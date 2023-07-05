# https://www.acmicpc.net/problem/13270
# 2인 1닭, 3인 2닭, 5인 3닭, 8인 5닭, 13인 8식의 피보나치
# 6이라면 => (2인 1닭 * 3) 혹은 (3인 2닭 * 2)
# 8이라면 => (2인 1닭*4) 혹은 (8인 5닭*1)
# https://www.acmicpc.net/problem/13270
# 2인 1닭, 3인 2닭, 5인 3닭, 8인 5닭, 13인 8식의 피보나치
# 6이라면 => (2인 1닭 * 3) 혹은 (3인 2닭 * 2)
# 8이라면 => (2인 1닭*4) 혹은 (8인 5닭*1)
from sys import stdin
N = int(stdin.readline().strip())
# (2,1) (3,2) (5,3) (8,5) (13,8)
a = set()
for i in range(1,N):
    if (N/i)==(N//i):
        a.add(N//i)

ans=[]

def fib(N):
    if N==0:
        return 1
    elif N==1:
        return 2
    elif N ==2:
        return 3
    else:
        return fib(N-1)+fib(N-2)
for i in range(1,N//2+1):
    ans.append([fib(i),fib(i-1)])
temp =[]
for i in ans:
    if i[0] in a:
        temp.append(N//i[0]*i[1])
print(temp[0],temp[1])