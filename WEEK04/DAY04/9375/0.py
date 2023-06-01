
# from sys import stdin
# from itertools import combinations

# T = int(stdin.readline().strip())
# for t in range(T):
#     N = int(stdin.readline().strip())
#     outfits = dict()
#     for _ in range(N):
#         items = list(stdin.readline().strip().split())
#         outfits[items[1]] = 1 if items[1] not in outfits else outfits[items[1]]+1
#     if len(outfits) == 1:
#         print(*outfits.values())
#     else:
#         looks = []
#         for i in range(2, N):
#             looks.extend(
#                 list(map(lambda i: i[0]*i[1], set(combinations(outfits.values(), i)))))
#         print(N+sum(looks))
# 메모리 초과 25%에서..

# logic
# dict() 활용해서 아이템 종류:[아이템1,2,..]로 입력값 받기 n(0 ≤ n ≤ 30)
# 종류가 하나밖에 없다면 (dict() 길이 1) 아이템 개수 리턴
# 여러 개라면 선택가능한 조합 (각 key에서 하나이상 선택)


from sys import stdin

T = int(stdin.readline().strip())
for t in range(T):
    N = int(stdin.readline().strip())
    outfits = dict()
    for _ in range(N):
        items = list(stdin.readline().strip().split())
        outfits[items[1]] = [items[0]] if items[1] not in outfits else [
            *outfits[items[1]], items[0]]
    if len(outfits) == 1:
        print(N)
    else:
        cnt = 1
        for i in outfits:
            cnt*= (len(outfits[i])+1)
        print(cnt-1)
