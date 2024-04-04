#Kruskal Algorithm
def find_parent(parent, x):
    if parent[x] != x:
        # parent[x] = find_parent(parent, #parent[x]# 이 부분 주의)
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

#parent 초기화
for i in range(1, v + 1):
    parent[i] = i

edge = []
result = 0

for _ in range(e):
    st, en, w = map(int, input().split())
    edge.append((w,st,en))

#비용이 낮은 edge부터 앞에 올 수 있게
edge.sort()

for ed in edge:
    w, st, en = ed
    st = find_parent(parent,st)
    en = find_parent(parent,en)
    if st != en:
        parent[st] = parent[en]
        result += w

print(result)