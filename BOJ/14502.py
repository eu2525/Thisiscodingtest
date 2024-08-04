from collections import deque
import copy

dx = [1, -1 ,0 ,0]
dy = [0, 0, 1, -1]

graph = []
row, col = map(int, input().split())
for _ in range(row):
    graph.append(list(map(int,input().split())))

# virus 위치 저장
max_num = 0
virus_que = deque()
for i in range(row):
    for j in range(col):
        if graph[i][j] == 2:
            virus_que.append((i,j))

wall_que = deque()

def make_wall(row_num, col_num):
    global max_num # global 변수인 max_num을 이용.
    # 벽을 다 세웠으면 진행
    if len(wall_que) == 3:
        result = dfs()
        max_num = max(result, max_num)
    else:
        for i in range(row_num, row):
            for j in range(col):
                if i == row_num and j < col_num:
                    continue
                if graph[i][j] == 0:
                    wall_que.append((i, j))
                    graph[i][j] = 1
                    make_wall(i, j)
                    wall_que.pop()
                    graph[i][j] = 0

def dfs():
    # 변수 Copy
    que = copy.deepcopy(virus_que)
    copy_graph = copy.deepcopy(graph)    

    # 바이러스 증식
    while que:
        x, y = que.pop()
        for idx in range(4):
            xx = x + dx[idx]
            yy = y + dy[idx]
            if xx >= 0 and xx < row and yy >= 0 and yy < col:
                if copy_graph[xx][yy] == 0:
                    copy_graph[xx][yy] = 2
                    que.append((xx,yy))

    # 안전 지역 수 세기
    cnt = 0
    for i in range(row):
        for j in range(col):
            if copy_graph[i][j] == 0:
                cnt += 1

    return cnt

make_wall(0, 0)

print(max_num)

