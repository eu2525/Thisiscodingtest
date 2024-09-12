# 모든 인접한 자리의 수가 총 몇개인지??
# 1 2 3 4 5 6 7 8 은 계단수가 2개씩 존재
# 0이랑 9는 1개씩만 존재
n = int(input())

dp = [1] * 10
dp[0] = 0

for _ in range(1, n):
    num_dp = [0] * 10
    num_dp[0] = dp[1]
    num_dp[9] = dp[8]
    for idx in range(1,9):
        num_dp[idx] = dp[idx - 1] + dp[idx + 1]
    dp = num_dp[:]

print(sum(dp) % 1000000000)