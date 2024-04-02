n = int(input())

food = list(map(int,input().split()))

dp = [0] * 101

dp[1] = food[0]
dp[2] = food[1]

for idx in range(3, n + 1):
    dp[idx] = max(dp[idx - 2], dp[idx - 3]) + food[idx - 1]

print(dp[n])