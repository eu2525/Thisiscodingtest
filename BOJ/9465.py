t = int(input())

for _ in range(t):
    col = int(input())
    dp = [[0] * (col + 1) for _ in range(2)]
    graph = []
    graph.append(list(map(int, input().split())))        
    graph.append(list(map(int, input().split())))
    dp[0][1] = graph[0][0]
    dp[1][1] = graph[1][0]
    for idx in range(1, col):
        dp[0][idx + 1] = max(max(dp[0][idx - 1],dp[1][idx - 1]), dp[1][idx]) + graph[0][idx]
        dp[1][idx + 1] = max(max(dp[0][idx - 1],dp[1][idx - 1]), dp[0][idx]) + graph[1][idx]

    print(max(dp[0][col], dp[1][col]))