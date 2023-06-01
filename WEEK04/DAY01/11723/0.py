# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 

from sys import stdin
M = int(stdin.readline().strip())

def calc(M:int):
    s = set()
    a = set(i for i in range(1,21))
    for _ in range(M):
        cmd = stdin.readline().strip().split()
        if cmd[0]=="add":
            s.add(int(cmd[1]))
        elif  cmd[0]=="remove":
            s.discard(int(cmd[1]))
        elif cmd[0]=="check":
            print(1) if int(cmd[1]) in s else print(0)
        elif cmd[0]=="toggle":
            s.discard(int(cmd[1])) if int(cmd[1]) in s else s.add(int(cmd[1]))
        elif cmd[0]=="all":
            s.update(a)
        elif cmd[0]=="empty":
            s.clear()
calc(M)