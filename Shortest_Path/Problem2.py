INF = int(1e9)
n, m = map(int,input().split())

graph = [[INF] * (n + 1) for _ in range(n+1)]

for i in range(n + 1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    st, en = map(int,input().split())
    graph[st][en] = 1
    graph[en][st] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[i][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])