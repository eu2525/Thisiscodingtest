from collections import deque

n, m = map(int, input().split())

visited = [[False] * m for _ in range(n)]                
graph = [[] for _ in range(n)]

for i in range(n):
    line = input()
    for j in range(m):
        graph[i].append(int(line[j]))


def dfs(graph, row, col):
    dx = [1, -1 , 0, 0]
    dy = [0, 0, 1 , -1]

    que = deque()
    que.append((row, col, 1))
    
    visited[row][col] = True
    
    while que:
        x, y, cnt = que.popleft()
        
        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx >= 0 and xx < n and yy >= 0 and yy < m:
                if visited[xx][yy] == False and graph[xx][yy] == 1:
                    visited[xx][yy] = True
                    que.append((xx, yy, cnt + 1))
                

result = dfs(graph, 0,0)

print(result)