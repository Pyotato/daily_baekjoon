# https://www.acmicpc.net/problem/10816
# dict에 card 담아서 dict에 이미 그 키가 있다면 카운트 증가 , 없다면 1
# 숫자가 dict에 있다면 그 개수 출력, 없다면 0 출력
from sys import stdin
N, cards = int(stdin.readline().strip()), list(
    map(int, stdin.readline().strip().split()))
M, num = int(stdin.readline().strip()), list(
    map(int, stdin.readline().strip().split()))
c = {}
for i in cards:
    c[i] = c[i]+1 if i in c else 1
for i in num:
    print(c[i], end=" ") if i in c else print(0, end=" ")
