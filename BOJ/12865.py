n, k = map(int,input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
costs = []

for idx in range(n):
    w, v = map(int,input().split())
    costs.append((w,v))

costs =sorted(costs, key = lambda x :(x[1]/x[0]), reverse=True)

for i in range(1, n + 1):
    item_w, item_v = costs[i - 1]
    for j in range(1, k + 1):
        dp[i][j] = dp[i-1][j]
        if j >= item_w:
            dp[i][j] = max(dp[i - 1][j - item_w] + item_v, dp[i][j])

print(max(dp[n]))
