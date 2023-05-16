# https://www.acmicpc.net/problem/10845
# logic
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

from sys import stdin
N = int(stdin.readline().strip())
cmds = [list(stdin.readline().strip().split()) for _ in range(N)]

def queue(c: list):
    ans = []
    for i in c:
        if i[0] == "push":
            ans.append(i[1])
        elif i[0] == 'front':
            print("-1") if len(ans) == 0 else print(ans[0])
        elif i[0] == 'back':
            print("-1") if len(ans) == 0 else print(ans[-1])
        elif i[0] == 'empty':
            print("1") if len(ans) == 0 else print("0")
        elif i[0] == 'pop':
            if len(ans) == 0:
                print("-1")
            else:
                print(ans[0])
                ans = ans[1:]
        elif i[0] == 'size':
            print(len(ans))

queue(cmds)
