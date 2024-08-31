alphabet_visited = [False] * 27
dx = [1, -1 , 0 , 0]
dy = [0, 0, 1, -1]
max_cnt = 0

row, col = map(int, input().split())
graph = [[''] * col for _ in range(row)] 

for i in range(row):
    line_text = input()
    for j in range(col):
        graph[i][j] = line_text[j]

def dfs(start_row, start_col, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for idx in range(4):
        x = start_row + dx[idx]
        y = start_col + dy[idx]
        if x >= 0 and x < row and y >=0 and y < col and not alphabet_visited[ord(graph[x][y]) - 65]:
            alphabet_visited[ord(graph[x][y]) - 65] = True
            dfs(x, y, cnt + 1)
            alphabet_visited[ord(graph[x][y]) - 65] = False         

alphabet_visited[ord(graph[0][0]) - 65] = True   
dfs(0, 0, 1)

print(max_cnt)