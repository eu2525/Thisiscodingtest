def find_parent(parents, idx):
    if parents[idx] != idx:
        parents[idx] = find_parent(parents, parents[idx])
    return parents[idx] 

def union(parents, st, en):
    root_st = find_parent(parents, st)
    root_en = find_parent(parents, en)
    if root_st != root_en:
        parents[root_st] = root_en

# 컴퓨터 수
n = int(input())

parents = [0] * (n + 1)

for idx in range(1, n + 1):
    parents[idx] = idx

# 쌍의 수
k = int(input())

for _ in range(k):
    st, en = map(int, input().split())
    union(parents, st, en)

virus_root = find_parent(parents, 1)
cnt = 0

for i in range(2, n+1):
    if find_parent(parents, i) == virus_root:
        cnt += 1

print(cnt)