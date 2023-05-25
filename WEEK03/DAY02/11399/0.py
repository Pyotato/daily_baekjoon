# logic
# 리스트에서 누적된 합의 최소를 구하기
# sort를 해서 현재 인덱스까지의 합을 구해주면 된다.
# 오름차순으로 리스트를 정렬해주면 합의 크기가 최소가 될 수 밖에 없기 때문
n = int(input())
p = list(map(int, input().split()))

p.sort()
ans = 0

for x in range(1, n+1):
    ans += sum(p[0:x])

print(ans)
