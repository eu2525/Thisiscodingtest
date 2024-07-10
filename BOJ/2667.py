from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
graph = []

visited = [[False] * n for _ in range(n)]


def dfs(row, col):
    cnt = 1
    que = deque()
    que.append((row, col))
    visited[row][col] = True
    while que:
        x, y = que.popleft()
        for idx in range(4):
            xx = x + dx[idx]
            yy = y + dy[idx]
            if (
                xx >= 0
                and xx < n
                and yy >= 0
                and yy < n
                and graph[xx][yy] == 1
                and not visited[xx][yy]
            ):
                visited[xx][yy] = True
                cnt += 1
                que.append((xx, yy))
    return cnt


for _ in range(n):
    graph.append(list(map(int, input())))

result_list = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs_cnt = dfs(i, j)
            result_list.append(dfs_cnt)

result_list.sort()

print(len(result_list))

for c in result_list:
    print(c)
