n = int(input())

num_list = list(map(int,input().split()))

# 가장 쉬운건 어떤 수를 기준으로 왼쪽 오른쪽을 셈.
left_dp = [1] * (n)
right_dp = [0] * (n)
dp = [1] * (n)

for idx, num in enumerate(num_list):
    for k in range(idx):
        if num_list[k] < num:
            left_dp[idx] = max(left_dp[idx], left_dp[k] + 1)

for idx in range(n - 1, -1, -1):
    num = num_list[idx]
    for k in range(idx , n):
        if num_list[k] < num:
            right_dp[idx] = max(right_dp[idx], right_dp[k] + 1)

for idx in range(n):
    dp[idx] = left_dp[idx] + right_dp[idx]

print(max(dp))