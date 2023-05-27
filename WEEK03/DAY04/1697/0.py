# logic
# +1 이동하거나 -1이동하거나 *2씩 이동했을 때
# 동생의 위치 K에 가장 적은 수로 이동
# bfs 로 이동가능한 경우 수들을 저장한 배열에서 가장 작은 값 리턴하기
# 덱을 사용해서 LIFO 시간복잡도 상수 시간되도록
# 수빈의 위치 N == 동생위치 K가 될때까지 
# 수빈 위치 N에서 +1, -1, *2하면서 
# 이동 횟수에 덱 끝에 추가
from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
MAX = 100001
ans = [0] * MAX


def find_sis(N: int) -> int:
    q = deque([N])
    while q:
        N = q.popleft()
        if N == K:
            return ans[N]
        for nxt in (N-1, N+1, 2*N):
            if 0 <= nxt < MAX and not ans[nxt]:
                ans[nxt] = ans[N]+1
                q.append(nxt)

print(find_sis(N))
