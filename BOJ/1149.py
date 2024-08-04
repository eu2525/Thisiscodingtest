n = int(input())

cost = [[0] * (3) for _ in range(n)]
house = []

for _ in range(n):
    house.append(list(map(int,input().split())))

cost[0] = house[0]

for i in range(1, n):
    cost[i][0] = min(cost[i-1][2], cost[i-1][1]) + house[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + house[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + house[i][2]

print(min(cost[n - 1]))