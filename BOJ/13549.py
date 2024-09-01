# 2 * x 하는건 0초 그니깐 지금 수의 2배 수는 모두 0초 인거지
# +1 , -1 은 1초
# 0-1 BFS 문제!

# 1) Deque의 Front에서 현재 Node를 꺼낸다.
# 2) 연결된 인접노드를 살펴본다
# 3) 현재 노드까지 소비된 비용 + 그 노드를 향한 가중치 <  그 노드 소비 비용 -> 소비 비용 갱신
# 4) 갱신되는 경우 노드로 가는 가중치가 0이면 Front로 1이면 Back에 삽입
# 5) Deque에서 더 이상 꺼낼 노드가 없을 때 까지 위 과정을 반복

from collections import deque

n, k = map(int, input().split())
dp = [1e9] * 100001

def bfs(start):
    global dp

    dp[start] = 0
    que = deque()
    que.append(start)

    while que:
        idx = que.popleft()
        for nx in (2 * idx, idx -1 , idx + 1):
            if nx > 100000 or nx < 0:
                continue

            if nx == 2 * idx:
                if dp[idx] < dp[nx]:
                    dp[nx] = dp[idx]
                    que.appendleft(nx)
            else:
                if dp[idx] + 1 < dp[nx]:
                    dp[nx] = dp[idx] + 1
                    que.append(nx)

bfs(n)

print(dp[k])