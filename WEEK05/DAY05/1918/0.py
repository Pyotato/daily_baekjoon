# 후위표기식
# 단항연산자 없다는 가정
from collections import deque
p = deque(input())
dq = deque()
while p:
    back=p.popleft()
    if back=="(":
        dq.append(back)
    elif (back == "+" or back == "-"):
        while (dq and dq[-1]!="("):
            print(dq.pop(),end="")
        dq.append(back)
    elif (back == "*" or back == "/"):
        while (dq and dq[-1]!="(" and (dq[-1] == "*" or dq[-1] == "/")):
            print(dq.pop(),end="")
        dq.append(back)
    elif back==")":
        while (dq and dq[-1]!="("):
            print(dq.pop(),end="")
        dq.pop()
    elif back.isalpha():
        print(back,end="")
while dq:
    print(dq.pop(),end="")
