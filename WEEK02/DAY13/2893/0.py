# https://www.acmicpc.net/problem/2893
# logic
# 배달하는 설탕 무게 N을 5와 3의 봉지 개수가 최소가 되도록
# 봉지 개수 == 몫
# 즉, N을 5와 3으로 나누었을 때 몫의 크기가 가장 작도록
# 5로 나누면 몫을 가장 적게 할 수 있으므로 N이 5로 나누어떨어지면 5로 나눈 몫을 리턴
# 안나누어 떨어지면 3으로 나눈 나머지로 다시 검사 
# N이 나누어떨어지지 않으면 -1리턴
from sys import stdin

N = int(stdin.readline().strip())
# 3<=N<=5000


def deliver(N: int) -> int:

    if N == 3 or N == 5:
        return 1
    else:
        count = 0
        while N >= 0:
            if N % 5 == 0:
                count += (N//5)
                return count
            N -= 3
            count += 1
        else:
            return -1


print(deliver(N))
