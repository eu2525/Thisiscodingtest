import heapq

n , m = map(int, input().split())
visited = [0] * (n+1)
for i in range(n + 1):
    visited[i] = i
edges = []
cnt = 0
result = 0

def find_parents(x, parents):
    if parents[x] != x:
        parents[x] = find_parents(parents[x], parents)
    return parents[x]

def union(st, en):
    global visited
    p = find_parents(st, visited)
    q = find_parents(en, visited)
    visited[p] = visited[q]

for _ in range(m):
    st, en, w = map(int, input().split())
    heapq.heappush(edges, (w, en,st))

while edges:
    w, en, st = heapq.heappop(edges)
    if cnt == n - 2:
        break
    if find_parents(st,visited) == find_parents(en,visited):
        continue
    result += w
    union(st,en)
    cnt += 1

print(result)