n, m = map(int,input().split())
x, y ,dir = map(int,input().split())


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0 for _ in range(m)] for _ in range(n)] 
#2차원 배열은 어케 생성...?
jido = []
for i in range(m):
    row = list(map(int,input().split()))
    jido.append(row)

visited[x][y] = 1

conti = False
cnt = 0


while(True):    
    #왼쪽을 살피는 코드    
    for i in range(1,4):
        next_dir = (dir - i) % 3
        nx = x + dx[next_dir]
        ny = y + dy[next_dir]
        if(nx >= 0 and nx < n and ny >= 0 and ny < n and visited[nx][ny] == 0 and jido[nx][ny] == 0):
            break
        if(i == 3):
            conti  = True

    # 모든 방향을 살폈는데도 갈 곳이 없는 경우
    if(conti == True):
        nx = x - dx[dir]
        ny = y - dy[dir]
        if(nx >= 0 and nx < n and ny >= 0 and ny < n and jido[nx][ny] == 0):
            x = nx
            y = ny
            conti = False
        else:
            break
    else:
        cnt += 1
        visited[nx][ny] = 1
        dir = next_dir
        x = nx
        y = ny
        

print(cnt)
    