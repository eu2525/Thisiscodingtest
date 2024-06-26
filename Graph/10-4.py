#서로소 집합을 이용한 사이클 판별 소스코드

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

cycle = False

for _ in range(e):
    st, en = map(int, input().split())
    if find_parent(parent, st) == find_parent(parent, en):
        cycle = True
        break
    else:
        union_parent(parent, st, en)

if cycle == True:
    print("싸이클이 존재합니다")
else:
    print("싸이클이 존재하지 않습니다.")