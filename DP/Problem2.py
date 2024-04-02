d = [30000] * 30001

n = int(input())

d[1] = 0

for i in range(1, n + 1):
    if( i * 5 <= 30000):
        d[i * 5] = min(d[i * 5], d[i] + 1)
    if(i * 3 <= 30000):
        d[i * 3] = min(d[i * 3], d[i] + 1)
    if(i * 2  <= 30000):
        d[i * 2] = min(d[i * 2], d[i] + 1)
    d[i + 1] = min(d[i + 1], d[i] + 1)

print(d[n])