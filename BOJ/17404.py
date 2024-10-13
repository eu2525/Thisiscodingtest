n = int(input())
house = []
for _ in range(n):
    house.append(list(map(int,input().split())))

result = 1e9

for idx in range(3):
    # 마지막 집의 색을 고정함.
    dp = [[0]* n for _ in range(n)]

    if idx == 0:
        dp[0][0] , dp[0][1], dp[0][2] = 1e9, house[0][1], house[0][2]
    elif idx == 1:
        dp[0][0] , dp[0][1], dp[0][2] = house[0][0], 1e9, house[0][2]
    else:
        dp[0][0] , dp[0][1], dp[0][2] = house[0][0], house[0][1], 1e9
    
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + house[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + house[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + house[j][2]

    result = min(result, dp[n - 1][idx])

print(result)
