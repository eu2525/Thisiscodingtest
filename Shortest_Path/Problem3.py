import heapq

n, m, c = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
d = [INF] * (n+1) 

for _ in range(m):
    st, en, w = map(int, input().split())
    graph[st].append((en,w))

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0,start))
    d[start] = 0
    while pq:
        cost, current = heapq.heappop(pq)
        if d[current] < cost:
            continue
        for i in graph[current]:
            next = i[0]
            next_cost = cost + i[1]
            if d[next] > next_cost:
                d[next] = next_cost
                heapq.heappush(pq,(next_cost, next))

dijkstra(c)

cnt = 0
distance = 0

for idx in range(1, n + 1):
    if d[idx] != INF:
        cnt +=1
        distance = max(distance, d[idx])

print(cnt - 1, distance)