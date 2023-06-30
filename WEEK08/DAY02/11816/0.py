from sys import stdin
X = list(map(lambda i: i,stdin.readline().strip()))
if len(X)>=2 and X[0]=='0'and X[1]!='x': #X는 8진수면 0이 주어짐
    print(int("".join(X),8))
elif len(X)>=2 and X[0]=='0' and X[1]=='x': # X는 16진수면 0x가 주어짐
    print(int("".join(X),16))
else: #10진수
     print("".join(X))

