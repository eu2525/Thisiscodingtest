import heapq
# min heap이구만...

v, e = map(int, input().split())

start_point = int(input())
edges = [[] for _ in range(v+1)]
cost = [1e9] * (v+1)

for _ in range(e):
    st, en, w = map(int, input().split())
    edges[st].append((en, w))

def dijkstra(start):
    global cost
    cost[start] = 0
    # Priority Queue
    pq = []  
    heapq.heappush(pq, (0,start))
    while pq:
        current_cost, current_point = heapq.heappop(pq)
        if current_cost > cost[current_point]:
            continue
        for next_point, next_point_cost in edges[current_point]:
            next_cost = next_point_cost + current_cost
            if next_cost < cost[next_point]:
                cost[next_point] = next_cost
                heapq.heappush(pq, (next_cost, next_point))

dijkstra(start_point)

for idx, value in enumerate(cost):
    if idx == 0:
        continue

    if value == 1e9:
        print("INF")
    else:
        print(value)