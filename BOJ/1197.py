import heapq

v, e = map(int,input().split())
visited = [i for i in range(v + 1)]
edges = []

for _ in range(e):
    st, en, w =  map(int, input().split())
    heapq.heappush(edges, (w,st,en))

def find_parents(a):
    if visited[a] != a:
        visited[a] = find_parents(visited[a])
    return visited[a]

def union(a,b):
    global visited
    p = find_parents(a)
    q = find_parents(b)
    visited[p] = q

result = 0
cnt = 0

while edges:
    w,st,en = heapq.heappop(edges)

    if cnt == v - 1:
        break

    if find_parents(st) != find_parents(en):
        result += w
        cnt += 1
        union(st,en)

print(result)