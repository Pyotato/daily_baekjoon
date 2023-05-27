# # https://www.acmicpc.net/problem/10814
# # logic
# from sys import stdin
# N = int(stdin.readline().strip())
# p = dict()
# for i in range(N):
#     age, person = map(str, stdin.readline().strip().split())
#     p[int(age)] = [person] if int(age) not in p else [
#         *p[int(age)], person]
# indx = min(p)
# while p:
#     a = p.pop(indx)
#     indx += 1
#     print(a[0]) if len(a) == 1 else print("\n".join(a))
