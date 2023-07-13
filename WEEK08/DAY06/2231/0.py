from sys import stdin
N = int(stdin.readline().strip()) # 1 ≤ N ≤ 1,000,000
for i in range(1,N+1): 
    n = sum((map(int, str(i)))) # i의 각 자릿수 더하기
    # print(str(i),list((map(int, str(i)))),n)
    accum = i+n
    if i==N: #입력값이 생성자와 같음 == 생성자 없음.
        print(0)
        continue
    if accum == N:
        print(i)
        break
