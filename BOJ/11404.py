n = int(input())
m = int(input())

dp = [[1e9] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 0 

for _ in range(m):
    st, en , w = map(int, input().split())
    dp[st - 1][en - 1] = min(dp[st - 1][en - 1], w)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][k] + dp[k][j] , dp[i][j])

for i in range(n):
    for j in range(n):
        if dp[i][j] == 1e9:
            print(0, end = ' ')
        else:
            print(dp[i][j] , end = ' ')
    print()

