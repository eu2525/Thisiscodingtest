from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

test_case = int(input())

def bfs(board, row, col, visited):
    n = len(board)
    m = len(board[0])
    visited[row][col] = True
    que = deque() # queue에 쌍으로 어케 넣냐...?
    que.append((row,col)) #아래와 같이 넣기!
    while que:
        row, col = que.popleft()
        for i in range(4):
            xx = row + dx[i]
            yy = col + dy[i]
            if(xx >= 0 and xx < n and yy >= 0 and yy < m):
                if(visited[xx][yy] == False and board[xx][yy] == 1):
                    visited[xx][yy] = True
                    que.append((xx, yy)) 
    return 1


for _ in range(test_case):
    m, n, k = map(int ,input().split())
    #배추 생성
    board = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m) ]

    for _ in range(k):
        row, col = map(int, input().split())
        board[row][col] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if(board[i][j] == 1 and visited[i][j] == False):
                bfs(board, i, j, visited)
                cnt += 1


    print(cnt)