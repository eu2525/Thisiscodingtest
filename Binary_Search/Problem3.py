n ,m = map(int,input().split())

dduck = list(map(int,input().split()))

start = 0
end = max(dduck)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for d in dduck:
        if (d > mid):
            total += (d - mid)
    if(total < m):
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)