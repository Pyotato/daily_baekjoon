
# from sys import stdin
# from collections import deque
# letter = deque(stdin.readline().strip()) #길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다
# bomb = list(stdin.readline().strip())
# tmp1 = deque()
# tmp2 = deque()
# while letter: 
#     a = letter.popleft()
#     if a in bomb:
#         tmp2.append(a)
#     if "".join(tmp2) == "".join(bomb):
#         tmp2 = []

#     elif a not in bomb:
#         tmp1.append(a)

# print("".join(tmp1)) if len(tmp1) > 0 else print("FRULA")
# 시간 초과

from sys import stdin
letter = stdin.readline().strip()
bomb = stdin.readline().strip()
stack = []
max_len = len(bomb)

for i in range(len(letter)):
    stack.append(letter[i])
    print(stack[-max_len:])
    if ''.join(stack[-max_len:]) == bomb:
        for _ in range(max_len):
            stack.pop()


print(''.join(stack))if stack else print('FRULA')
