n = int(input())
dp = []
for idx in range(n):
    dp.append(list(map(int, input().split())))

for idx in range(1, n):
    for j in range(idx + 1):
        if j == 0:
            dp[idx][j] = max(dp[idx - 1][j] + dp[idx][j], dp[idx][j])
        elif j == idx:
            dp[idx][j] = max(dp[idx - 1][j - 1] + dp[idx][j], dp[idx][j])
        else:
            dp[idx][j] = max(
                max(dp[idx - 1][j - 1], dp[idx - 1][j]) + dp[idx][j], dp[idx][j]
            )

result = max(dp[n - 1])

print(result)
