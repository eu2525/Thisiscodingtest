import heapq

result = 0
n, k = map(int, input().split())
jewel = []
bags = []

for _ in range(n):
    m, v = map(int,input().split())
    jewel.append((m, v))

for _ in range(k):
    bags.append(int(input()))

jewel.sort()
bags.sort(reverse = True)

result = 0
tmp = [] 

for bag in bags:
    while jewel:
        weight, value = jewel.pop()
        print(bag, jewel, tmp, weight, value)
        if bag >= weight:
            heapq.heappush(tmp, - value)

    print(bag, jewel, tmp)

    if tmp:
        result -= heapq.heappop(tmp)

print(result)