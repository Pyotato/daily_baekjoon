# https://www.acmicpc.net/problem/10866

from sys import stdin
N = int(stdin.readline().strip())
cmds = [list(stdin.readline().strip().split()) for _ in range(N)]


def deque(c: list):
    ans = []
    for i in c:
        if i[0] == "push_front":
            ans = [i[1], *ans]
        elif i[0] == "push_back":
            ans.append(i[1])
        elif i[0] == 'pop_front':
            print(ans[0]) if len(ans) != 0 else print("-1")
            ans = ans[1:] if len(ans) != 0 else ans

        elif i[0] == 'pop_back':
            print(ans[-1]) if len(ans) != 0 else print("-1")
            ans.pop() if len(ans) != 0 else ans
        elif i[0] == 'size':
            print(len(ans))
        elif i[0] == 'empty':
            print("1") if len(ans) == 0 else print("0")
        elif i[0] == 'front':
            print("-1") if len(ans) == 0 else print(ans[0])
        elif i[0] == 'back':
            print("-1") if len(ans) == 0 else print(ans[-1])


deque(cmds)
