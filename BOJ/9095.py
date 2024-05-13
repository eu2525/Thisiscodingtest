T = int(input())

dp = [0, 1 ,2, 4]

for idx in range(4, 12):
    dp.append(dp[idx - 3] + dp[idx - 2] + dp[idx - 1])


for _ in range(T):
    n = int(input())
    print(dp[n])