n = int(input())

graph = []

max_dp = [0 ,0, 0]
min_dp = [0, 0, 0]

for i in range(n):
    row1, row2, row3 = map(int, input().split())
    if i == 0:
        max_dp[0], max_dp[1] , max_dp[2] = row1, row2, row3
        min_dp[0], min_dp[1] , min_dp[2] = row1, row2, row3
    else:
        max_num1 = max(max_dp[0], max_dp[1]) + row1
        max_num2 = max(max_dp) + row2
        max_num3 = max(max_dp[1], max_dp[2]) + row3
        min_num1 = min(min_dp[0], min_dp[1]) + row1
        min_num2 = min(min_dp) + row2
        min_num3 = min(min_dp[1], min_dp[2]) + row3
        max_dp[0], max_dp[1] , max_dp[2] = max_num1, max_num2, max_num3
        min_dp[0], min_dp[1] , min_dp[2] = min_num1, min_num2, min_num3      

print(max(max_dp), min(min_dp))