import heapq

# 도시 수
n = int(input())
# 버스 수
m = int(input())

graph = [[] for _ in range(n + 1)]
d = [1e9] * (n + 1)

for _ in range(m):
    st, en, w = map(int, input().split())
    graph[st].append((en, w))

start_point , end_point = map(int, input().split())

def dfs(st_p):
    d[st_p] = 0
    pq = []
    heapq.heappush(pq, (st_p, 0))
    while pq:
        current_point , current_cost = heapq.heappop(pq)
        if d[current_point] < current_cost:
            continue
        for next_point, w in graph[current_point]:
            next_cost = w + current_cost
            if next_cost < d[next_point]:
                d[next_point] = next_cost
                heapq.heappush(pq, (next_point, next_cost))



dfs(start_point)

print(d[end_point])