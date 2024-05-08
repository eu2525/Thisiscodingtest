import math

n, k = map(int, input().split())

coin = []

for i in range(n):
    co = int(input())
    coin.append(co)

coin.sort(reverse= True)

result = 0
for co in coin:
    if k == 0:
        break

    if k >= co:
        x = k / co
        x = math.floor(x)
        result += x
        k -= (x * co)

print(result)    