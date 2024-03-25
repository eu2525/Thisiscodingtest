n, m = map(int, input().split())

min_num = 0

for i in range(n):
    data = map(int, input().split())
    min_num = max(min(data), min_num)

print(min_num)