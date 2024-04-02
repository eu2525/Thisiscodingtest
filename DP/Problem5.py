n , m = map(int,input().split())

coin = []

dp = [10001] * 10001

for _ in range(n):
    c = int(input())
    dp[c] = 1
    coin.append(c)

for idx in range(m + 1):
    for co in coin:
        if idx - co <= 0:
            break
        if dp[idx - co] != 10001:
            dp[idx] = min(dp[idx],dp[idx - co] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])