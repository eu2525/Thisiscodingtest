from collections import deque

col, row = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1,- 1]

def dfs(que, graph):
    max_num = 0
    while que:
        current_point = que.popleft()
        r = current_point[0][0]
        c = current_point[0][1]
        num = current_point[1]
        max_num = max(max_num, num)
        for i in range(4):
            xx = r + dx[i]
            yy = c + dy[i]
            if(xx >= 0 and xx < len(graph) and yy >= 0 and yy < len(graph[0])):
                if graph[xx][yy] == 0:
                    graph[xx][yy] = 1
                    que.append(((xx,yy),num+1))

    return graph, max_num




#이차원 그래프 입력 받는법
graph = []
for _ in range(row):
    new_list = list(map(int,input().split()))
    graph.append(new_list)

q = deque()

for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:
            q.append(((i,j),0))

new_graph, print_num = dfs(que = q, graph = graph)
complete = False

for i in range(row):
    for j in range(col):
        if new_graph[i][j] == 0:
            complete = True

if complete:
    print(-1)
else:
    print(print_num)
