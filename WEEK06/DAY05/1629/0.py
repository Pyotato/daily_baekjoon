# logic
# 해당 문제는 divide & conquer 
# 즉 큰 문제를 작게 쪼개서 해결하면 가능
# 핵심은 구하려는 거를 반복해서 문제를 작게 만들기
# 현재의 문제는 어떤수 A를 B번 제곱했을 경우 C로 나눈 나머지를 구하려고 한다.
# 지수가 1일 경우는 구하려는 바를 바로 리턴해주면 되지만
# 지수가 2이상알 경우는 나머지의 규칙성을 활용해서 리턴해주면 됨
# 10 11 12 라고 하면
# (10^1) % 12 == 제곱수의 나머지
# (10^2) % 12 = (전의 제곱수*10)%12 ,전의 제곱수 ==전의 제곱수*10
# (10^3) % 12 = ((10^2)*10)%12 = ((10^2)*10)%12 
# (10^4) % 12 = ((10^3)*10)%12 = (((10^2)* (10^2)))%12 
# (10^5) % 12 = ((10^4)*10)%12 =(((10^2)*(10^2)*10))%12 
# 식으로 제곱할 수가 짝수면 제곱을 두번해주면 됨 (지수 곱셈법칙)
# 식으로 제곱할 수가 홀수면 제곱을 두번해주고 더해주면 됨 

import sys
A,B,C =list(map(int,sys.stdin.readline().split()))
def sol(A,N):
    if N==1: #지수가 1
        return A%C
    else:
        recur=sol(A,N//2) #지수법칙사용
        if N%2==0: #만약 지수가 짝수라면
            return (recur*recur) %C
        else:
            return (recur*recur*A)%C
print(sol(A,B))