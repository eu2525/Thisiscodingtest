t = int(input())

dp = [0] * 101

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3

for i in range(7 , 101):
    dp[i] = dp[i-1] + dp[i - 5]

for _ in range(t):
    num = int(input())
    print(dp[num])