n = int(input())

stair = [0] * (n + 1)
for idx in range(1, (n + 1)):
    score = int(input())
    stair[idx] = score

dp = [[0] * 2 for _ in range(n + 1) ]
dp[1][0] = stair[1]

for i in range(2, len(dp)):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stair[i]
    dp[i][1] = dp[i-1][0] + stair[i]

print(max(dp[n][0], dp[n][1]))