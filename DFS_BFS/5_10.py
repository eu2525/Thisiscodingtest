from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n) ]

graph = []
for i in range(n):
    graph.append(list(map(int,input())))
'''
아래의 코드를 위와 같이 간단히 표현 가능.
graph = [[] for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(len(row)):
        graph[i].append(int(row[j]))
'''

def bfs(row, col):
    visited[row][col] = True
    que = deque() # queue에 쌍으로 어케 넣냐...?
    que.append((row,col)) #아래와 같이 넣기!
    while que:
        row, col = que.popleft()
        for i in range(4):
            xx = row + dx[i]
            yy = col + dy[i]
            if(xx >= 0 and xx < n and yy >= 0 and yy < m and visited[xx][yy] == False and graph[xx][yy] == 0):
                visited[xx][yy] = True
                que.append((xx, yy)) # append는 list 자체를 넣고, extend는 list의 각 항목들을 넣음. 
                                     #  -> a.append(['ping','pong']) 하면 리스트가 들어가고 extend하면 'ping','pong'이 들어감
    
    return 1

result = 0
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0 and visited[i][j] == False):
            result += bfs(i,j)

print(result)