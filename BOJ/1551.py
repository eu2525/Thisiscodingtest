n, k = map(int, input().split())

a = list(map(int,input().split(',')))

b = a

for _ in range(k):
    a = b
    b = []
    for i in range(len(a) - 1):
        b.append(a[i + 1] - a[i])

for idx in range(len(b) - 1):
    print(b[idx] , end = ',')
print(b[len(b) - 1])