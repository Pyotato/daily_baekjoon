from itertools import combinations
from sys import stdin

while True:
    num = list(map(int, stdin.readline().strip().split()))
    if num[0] == 0:
        break
    else:
        print(
            "\n".join(map(lambda i: " ".join(map(str, i)), combinations(num[1:], 6))))
        print()
