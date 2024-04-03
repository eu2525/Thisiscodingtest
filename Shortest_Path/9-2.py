import heapq
INF = int(1e9)

n, m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
d = [INF] * (n + 1)

for _ in range(m):
    st, en, w = map(int,input().split())
    graph[st].append((en,w))

def dijkstra(start):
    # Priority Queue를 위한 List와 heapq
    q = []
    heapq.heappush(q,(0,start))
    #start는 출발점이라 d 배열을 0으로 초기화
    d[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 지금 거리보다 짧은 경우는 Pass
        if d[now] < dist:
            continue

        for i in graph[now]:
            next = i[0]
            cost = dist + i[1] 
            if cost < d[next]:
                d[next] = cost
                heapq.heappush(q,(cost, next))

dijkstra(start)

for i in range(1, n + 1):
    if d[i] == INF:
        print("INFINITY")
    else:
        print(d[i])
