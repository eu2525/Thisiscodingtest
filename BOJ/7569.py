# 토마토가 있음
# 하루가 지나면 익은 토마토 인접한 안익은 토마토가 익게 된다.
# 인접한 토마토 위, 아래, 동, 서, 남, 북
# 1 : 익은 토마토 , 0 : 익지 않은 토마토 -1 : 토마토가 들어있지 않은 칸 
from collections import deque

graph = []
que = deque()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# M : 세로 칸 , N : 가로 칸 , H : 높이
M, N, H = map(int, input().split())

for i in range(H):
    layer = []
    for j in range(N):
        input_row = list(map(int,input().split()))
        for idx, num in enumerate(input_row):
            if num == 1:
                # floor, row, col, 카운트
                que.append((i, j, idx, 0))
        layer.append(input_row)        
    graph.append(layer)

max_cnt = -1

def dfs():
    global que, max_cnt

    while que:
        floor, row, col, cnt = que.popleft()
        max_cnt = max(max_cnt, cnt)
        for i in range(6):
            x = row + dx[i] 
            y = col + dy[i]
            z = floor + dz[i]
            if z < H and z >= 0 and y < M and y >= 0 and x < N and x >= 0:
                if graph[z][x][y] == 0:
                    graph[z][x][y] = 1
                    que.append((z, x, y, cnt + 1))

dfs()

complete = True

for h in range(H):
    for n in range(N):
        for m in range(M):
            # 층, row, col 
            if graph[h][n][m] == 0:
                complete = False

if complete:
    print(max_cnt)
else:
    print(-1)