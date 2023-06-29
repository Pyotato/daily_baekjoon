from sys import stdin
N = int(stdin.readline().strip()) #1 ≤ N ≤ 10,000,000
if 1<N<=3:
    print(N)
else :
    i=2
    while N!=1:
        if N%i==0:
            N=N//i
            print(i)
        else: 
            i+=1