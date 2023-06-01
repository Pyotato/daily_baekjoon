# logic
# N이 주어졌을 때 N==0이면 0 counter1+1, N==1이면 counter2+1, N>2이면 (N-1)연산값+(N-2)연산값 리턴
# N = 3 일 때 : 2일때 + 1일때 합 -> (1일때 +0일때) + (1일 때)
# N = 4 일 때 : 3일때 + 2일때 합 -> (2일때 + 1일때) + (1일때 + 0일때) -> ((1일때 + 0일때)+ 1일때) + (1일때 + 0일때)
# N = 5 일 때 : 4일때 + 3일때 합 -> (3일때 + 2일때) + (2일때 + 1일때) ->((2일때 + 1일때) + (1일때 + 0일때)) + ((1일때 + 0일때)+ 1일때)
# 0일 때 = 0 호출 1번, 1 호출 0번
# 1일 때 = 0호출 0번, 1 호출 1번
# 1일때 + 0일 때 = 0 호출 1번,1 호출 1번
# dp로 호출 횟수 패턴으로 풀기
from sys import stdin
T = int(stdin.readline().strip())

zeros = [1,0,1]
ones = [0,1,1]
def f(n):
    if n>=len(zeros):
        for i in range(len(zeros),n+1):
            zeros.append(zeros[i-1]+zeros[i-2])
            ones.append(ones[i-1]+ones[i-2])
    print(" ".join([str(zeros[n]),str(ones[n])]))
for i in range(T):
    N = int(stdin.readline().strip())
    f(N)
