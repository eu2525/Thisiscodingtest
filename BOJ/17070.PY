N = int(input())
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

# 상태 (r, c, d) 가로 세로 대각선
# 마지막 위치만 저장
dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            if graph[i][j+1] != 1:
                dp[i][j+1][0] += (dp[i][j][0] + dp[i][j][2]) 
        if i + 1 < N:
            if graph[i + 1][j] != 1:
                dp[i+1][j][1] += (dp[i][j][1] + dp[i][j][2])
        if i + 1 < N and j + 1 < N:
            if graph[i + 1][j] != 1 and graph[i][j+1] != 1 and graph[i+1][j+1] != 1:
                dp[i+1][j+1][2] += (dp[i][j][0] + dp[i][j][1] + dp[i][j][2])

print(sum(dp[N-1][N-1]))
