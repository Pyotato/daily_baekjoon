from sys import stdin

N = int(stdin.readline().strip())
ans = dict()
for _ in range(N):
    age, name = stdin.readline().strip().split()
    if int(age) not in ans:
        ans[int(age)] = [name]
    else:
        ans[int(age)] = [*ans[int(age)], name]
while ans:
    min_ = min(ans.keys())
    for i in ans[min_]:
        print("{age} {name}".format(age=min_, name=i))

    ans.pop(min_)
