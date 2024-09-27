n = int(input())
grape = []

for _ in range(n):
    grape.append(int(input()))

# 현재 잔을 안마시는 경우 : 2
# 이전에 있던 잔을 마시고 이번 잔도 마시는 경우 : 1
# 이전에 있던 잔을 안 마시고, 현재 잔은 마시는 경우 : 0
# 2차원 DP로 풀어보자
dp = [[0] * n for _ in range(3)]

dp[0][0] = grape[0]

for i in range(1, n):
    dp[0][i] = dp[2][i-1] + grape[i]
    dp[1][i] = dp[0][i - 1] + grape[i]
    dp[2][i] = max(dp[0][i - 1], max(dp[1][i-1], dp[2][i - 1]))

print(max(max(dp[0]), max(max(dp[1]), max(dp[2]))))