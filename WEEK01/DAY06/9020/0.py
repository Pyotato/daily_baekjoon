# https://www.acmicpc.net/problem/9020
# logic
# 골드바흐 수 = 짝수인 수를 두 소수의 합으로 표현 가능한 수
# 핵심 : 소수 구하기
# 소수 : 1과 자신 이외에 약수가 없는 3 이상의 수
# 값에 루트를 씌웠을 때 정수가 되면 자기 자신이외에 나뉘는 값이 있다는 뜻
# 짝수를 루트를 씌우면 2의 짝수 제곱인 수는 나누어 떨어진다
# 예를 들어 √16 =√4²=4 이지만 √8 = √2³ = 2.xxx
# 자기자신까지 나누어주지 않아도  
# 자기를 루트씌운 값까지 나눠줄 떄 
#나머지가 생기지 않는다면 소수가 아니다.

from sys import stdin
T = int(stdin.readline().strip())
n = [int(stdin.readline().strip()) for _ in range(T)]


def is_prime(n:int):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1): #루트씌운 값 
        if n % i == 0: 
            return False
    return True

def goldbach(N: list):
    for num in N: 
        a, b = num//2, num//2 
        while a > 0: 
            if is_prime(a) and is_prime(b): 
                print(a,b)
                break
            else: #아니면 6,6 -> 5,7 식으로 빼주고 더해줌
                a -= 1
                b += 1
    
goldbach(n)
