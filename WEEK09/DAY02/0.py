from collections import deque
from sys import stdin

N = int(stdin.readline().strip())  # 1 ≤ N ≤ 500,000
cards = set(map(int, stdin.readline().strip().split()))
M = int(stdin.readline().strip())  # 1 ≤ M ≤ 500,000
nums = deque(map(int, stdin.readline().strip().split()))
# 가지고 있으면 1을 (False), 아니면 0을 공백 (True)
while nums:
    n = nums.popleft()
    print("0", end=" ") if cards.isdisjoint({n}) else print("1", end=" ")
