# n명의 학생 들
# 두 학생의 키를 비교해서 키를 비교
# 왠지 그 위상 정렬? 같은데

from collections import deque

n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]
que = deque()

for _ in range(m):
    fir, sec = map(int, input().split())
    graph[fir].append(sec)
    indegree[sec] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)

while que:
    idx = que.popleft()
    print(idx, end = ' ')
    for next_pos in graph[idx]:
        indegree[next_pos] -= 1
        if indegree[next_pos] == 0:
            que.append(next_pos)
