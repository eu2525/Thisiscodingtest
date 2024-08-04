n = int(input())

dp = [1] * n
num_list = list(map(int,input().split()))


for idx in range(n):
    for j in range(idx):
        if num_list[idx] > num_list[j]:
            dp[idx] = max(dp[idx], dp[j] + 1)

print(max(dp))