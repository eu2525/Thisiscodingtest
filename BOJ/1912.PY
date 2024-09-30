n = int(input())
num_list = list(map(int,input().split()))

# 새로 시작 vs 그전꺼에서 지금 더 한거
dp = [0] * n 
dp[0] = num_list[0]

for id in range(1, n):
    dp[id] = max(dp[id - 1]+ num_list[id],num_list[id])

print(max(dp))