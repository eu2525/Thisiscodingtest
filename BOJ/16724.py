# 성우가 피리를 불면 회원들이 움직임
# U(위), D(아래), L(왼쪽), R(오른쪽) 4가지 방향으로 움직임.
# SAFE ZONE에 무조건 들어갈 수 있게 만드는 수를 적어라

N , M = map(int,input().split())

parents = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
graph = [[] for _ in range(N)]

for r in range(N):
    line = input()
    for c in range(M):
        parents[r][c] = r * N + c
        graph[r].append(line[c])

cnt = 0 

def dfs(row, col, idx):
    global visited, parents, cnt
    if visited[row][col] and parents[row][col] == idx:
        cnt += 1
    
    if not visited[row][col]:
        visited[row][col] = True
        parents[row][col] = idx
        dir = graph[row][col]

        if dir == 'D':
            dfs(row + 1, col, idx)
        elif dir == 'U': 
            dfs(row - 1, col, idx)
        elif dir == 'L': 
            dfs(row, col - 1, idx)
        elif dir == 'R': 
            dfs(row , col + 1, idx)
    
for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            index_num = r * M + c
            dfs(r, c, index_num)

print(cnt)