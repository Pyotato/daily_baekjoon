# https://www.acmicpc.net/problem/2609
# logic
# 최대 공약수 : 유클리드 호제법
# 두 수 a와 b가 있을 때, b가 0이 되기 전까지 a를 b로 나누어준 나머지가 최대 공약수가 된다
# 최소 공배수 : 두 수를 곱해준 값을 최대 공약수로 나눈 값이 최대 공약수가 된다
# 24 18 
# 24 = 2*2*3
# 18 = 2*3*3
# 최소 공배수 = (2*2*3)*(2*3*3)/(2*3) = 3*2*3*3 = 72

from sys import stdin
N,M = map(int,stdin.readline().strip().split())
#유클리드 호제법
def GCD(a : int, b : int) -> int:
    while b > 0:
        a , b = b , a%b
    return a
#최소공배수
def LCM(a : int, b : int) -> int:
    return (a * b) // GCD(a,b)

#최대공약수
def GCD_LCM(n : int , m : int)->str:
    print(str(GCD(n , m))+"\n"+str(LCM(n , m)))

GCD_LCM(N,M)
