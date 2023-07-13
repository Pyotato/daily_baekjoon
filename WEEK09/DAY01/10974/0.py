from itertools import permutations
from sys import stdin

N = int(stdin.readline().strip())
print("\n".join(map(lambda i: " ".join(map(str, i)), permutations(range(1, N+1), N))))
