from sys import stdin
from collections import deque
from itertools import permutations
N = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().strip().split()))
nums = deque(nums)
calc = dict()
calc["+"], calc["-"], calc["*"], calc["/"] = list(
    map(int, stdin.readline().strip().split()))
ops = {"+": (lambda a, b: a+b), "-": (lambda a, b: a-b),
       "*": (lambda a, b: a*b), "/": (lambda a, b: a//b if a*b > 0 else -(abs(a)//abs(b)))}
ans = []
dq = deque(set(permutations(
    [*["+"]*calc["+"], *["*"]*calc["*"], *["-"]*calc["-"], *["/"]*calc["/"]], N-1)))
while dq:
    calcs = dq.popleft()
    idx = 0
    temp = deque()
    for i in nums:
        if not temp:
            temp.append(i)
            continue
        if len(temp) == 1:
            temp.append(i)
        if len(temp) == 2:
            a, b = temp.popleft(), temp.popleft()
            temp.append(ops[calcs[idx]](*[a, b]))
            idx += 1
    ans.append(*temp)
print(max(ans))
print(min(ans))
