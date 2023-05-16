# https://www.acmicpc.net/problem/1018
# logic
# 체스판입력값은 W와 B로 되어있지만 보기 편하게 입력값을 B=0, W=1로 변경
# 체스판은 8x8이고 01 01 01 01 로 시작되거나 10 10 10 10 로 칠해져야함
# 체스판의 넓이가 8x8 일때는 두 경우 중 바꿔칠해야하는 경우가 최소가 되는 경우를 구하면됨
# 바꿔칠해야하는 것의 여부는 이중 for문을 돌리면 된다.
    #  0으로 시작하는 경우
        # 바깥 for문이 짝수 행일 때 안쪽 for문의 짝수 열이 0이어야하고 홀수 열이 1이어야함
        # 아닌 경우 count 변수에 +1해준다
    # 1로 시작하는 경우는 위의 경우의 반대이다. 
# count변수는 바꿔줘야하는 경우의 합이므로
# 합들을 배열에 담아서 그 중 가장 최소를 답으로 리턴한다.
# 체스판의 넓이는 8x8로 고정되어 있다.
# for문을 돌아주면서 8x8으로 체스판을 짤라주면서
# 마찬가지로 합들을 담은 배열의 최소가 답이 된다.

from sys import stdin
N, M = map(int, stdin.readline().strip().split())
c = [stdin.readline().strip() for _ in range(N)]
c = list(map(lambda i: list(0 if j == "B" else 1 for j in i), c))  # B ==0, W==1

def c_start(n,m,start,end):
    cnt=0
    for i in range(n,n+8):
        # 0,2,4,6번쨰 행
        if i%2==0:
            for j in range(m,m+8):
                if j%2==0: #0,2,4,6번쨰 열
                    cnt=cnt+1 if c[i][j]==start else cnt
                if j%2==1: #1,2,5,7번쨰 열
                    cnt=cnt+1 if c[i][j]==end else cnt
        # 1,3,5,7번쨰 행
        else:
            for j in range(m,m+8):
                if j%2==0:#0,2,4,6번쨰 열
                    cnt=cnt+1 if c[i][j]==end else cnt
                if j%2==1:#1,2,5,7번쨰 열
                    cnt=cnt+1 if c[i][j]==start else cnt     
    return cnt

def clr_board (n,m):
    ans=[]
    for i in range(0,n-7):  
        for j in range(0,m-7):
            ans.append(c_start(i,j,0,1))
            ans.append(c_start(i,j,1,0))
    return min(ans)     

print(clr_board(N,M))