n, m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + graph[i][j]
    
for _ in range(m):
    f_x, f_y, s_x , s_y = map(int, input().split()) 
    cnt = dp[s_x][s_y] - dp[f_x - 1][s_y] - dp[s_x][f_y - 1] + dp[f_x - 1][f_y  - 1] 
    print(cnt)