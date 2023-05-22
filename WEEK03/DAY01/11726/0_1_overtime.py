# logic
# 2 x n 직사각형
# 2와 1의 조합으로 n이 되는 경우
# 3=> 111 와 21 일 경우 
# 21은 21과 12두 경우가 있음
# 10007 로 나눈 나머지 구하기
N = int(input())
from itertools import permutations

def rect(N):
    if N==1:
        return 1
    if N==2:
        return 2
    arr =[[2 for _ in range(1*(i+1))] for i in range(N//2)]
    s = 0
    for i in range(len(arr)):
        ones = N-sum(arr[i])
        arr[i]=[*arr[i], *[1]*ones]
        print(arr[i])
        s+=(len(set(permutations(arr[i])))%1007)
    return s+1


print(rect(N))


##시간 초과###
