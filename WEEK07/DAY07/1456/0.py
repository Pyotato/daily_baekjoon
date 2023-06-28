# from collections import deque
# A, B = map(int, stdin.readline().strip().split()) #1 ≤ A ≤ B ≤ 10^14
# A =2 if A<=2 else A
# ans = set(map(lambda i: i,range(A,B+1)))
# ans = deque(ans)
# temp =set()
# def find_prime(ans):
#     while ans:
#         i = ans.popleft()
#         ans =deque(filter(lambda j: j%i!=0,ans))
#         temp.add(i)
#     return temp

# def find_nearly_prime(temp):
#     cnt=0
#     for i in temp:
#         exp = 2
#         while pow(i,exp)<=B:
#             cnt+=1
#             exp+=1
#     return cnt
# print(find_prime(ans))
# 메모리 초과

# 에라토스태네스의 채

import sys
input = sys.stdin.readline()

m, n = map(int, input.split())

dv= int(pow(n,0.5)) #n의 약수는 (n ** 0.5) 이하(n의 제곱근). 따라서 (n ** 0.5)까지만 계산하기
are_prime = [True] * (dv + 1) #소수여부 판별 리스트
are_prime[1] = False
for i in range(2, dv + 1): #소수 여부 따지기
    if are_prime[i]:
        if i * i > dv:
            break
        for j in range(pow(i,2), dv + 1, i):
            are_prime[j] = False

count = 0
for i in range(1, len(are_prime)): #거의 소수 여부 따지기
    if are_prime[i]:
        res = i * i
        while True:
            if res < m:
                res *= i
                continue
            if res > n:
                break
            res *= i
            count += 1

print(count)