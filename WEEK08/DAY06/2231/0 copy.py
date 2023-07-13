# 가장 작은 생성자 구하기
# 198 + 1 + 9 + 8 = 216
# 100*1 + 10*9 + 1*8 + 1 + 9 + 8 = 216
from sys import stdin
from itertools import combinations
N = list(map(int, stdin.readline().strip())) # 1 ≤ N ≤ 1,000,000
N_num = int("".join(list(map(str,N))))
N_len = len(N)
nums = [i for i in range(10)]
ans = []

def get_constructor(n:list):
    n_arr = list(map(int,n))
    r = 0
    for i in range(len(n_arr)):
        r+=pow(10,len(n_arr)-1-i)*n_arr[i]
        r+=n_arr[i]
    return r
temp = [0]if N_num[0]==0 else []

for i in range(N_len): # 자릿수
    for j in nums:
            if pow(10,i)*j < N_num:
                if j!=0:
                    temp.append(pow(10,i)*j)
print(temp)