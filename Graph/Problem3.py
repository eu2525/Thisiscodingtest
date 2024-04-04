#길을 없애 -> Kruskal 알고리즘

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[a] = b

n , m = map(int, input().split())
town = [0] * (n + 1)

for i in range(1 , n + 1):
    town[i] = i

edge = []
result = 0

for _ in range(m):
    st, en , w = map(int, input().split())
    edge.append((w, st, en))

edge.sort()

cnt = 0
#마을을 2개로 나눔 다 하나로 합치는게 아님!
for ed in edge:
    # edge가 n-1개이면 모든 node를 연결하기 때문에 n-2개이면 2개의 마을로 관리 가능.
    if cnt == n - 2:
        break
    w, st, en = ed
    p = find_parent(town, st)
    q = find_parent(town, en)
    if p != q:
        town[p] = q
        result += w
        cnt += 1
    

print(result)