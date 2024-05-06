from collections import deque

n,  m , v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    st , en = map(int, input().split())
    graph[st].append(en)
    graph[en].append(st)

# 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
for id in range(1, n+1):
    graph[id].sort()

def bfs(graph, start, visited):
    que = deque()
    que.append(start)
    visited[start] = True
    while que:
        idx = que.popleft()
        print(idx, end = ' ')
        for num in graph[idx]:
            if(visited[num] == False):
                visited[num] = True
                que.append(num)

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end = ' ')
    for num in graph[start]:
        if visited[num] == False:
            dfs(num, visited)


visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)