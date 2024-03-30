n, m = map(int,input().split())

visited = [[False] * m for _ in range(n)]

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))


min_cnt = 99999999999

def dfs(row, col, cnt):
    global min_cnt #전역 변수 선언

    if(row < 0 or row >= n or col < 0 or col >= m or graph[row][col] == 0 or visited[row][col] == True):
        return
    
    if (row == (n - 1) and col == (m - 1)):
        min_cnt = min(min_cnt, cnt)  # 현재 cnt와 이전의 min_cnt 중 작은 값을 선택하여 min_cnt에 저장
        return
    
    visited[row][col] = True

    dfs(row + 1, col, cnt + 1)
    dfs(row, col + 1, cnt + 1)
    dfs(row - 1, col, cnt + 1)
    dfs(row, col - 1, cnt + 1)

dfs(0,0,1)

print(min_cnt)