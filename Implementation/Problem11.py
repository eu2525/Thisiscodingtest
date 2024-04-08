from collections import deque
# right = 0 , down = 1 , left = 2, up = 3
dir = [(0,1), (1,0), (0,-1), (-1, 0)]

# n은 보드의 크기.
n = int(input())
board = [[0] * (n + 1)  for _ in range(n + 1)]

# k는 사과의 수
k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    board[row][col] = -1


change_dir = {}

#방향 전환 수
L = int(input())
for _ in range(L):
    t, d = input().split()
    t = int(t)
    change_dir[t] = d


que = deque()

que.append((1,1))
d = 0
cnt = 0
#dictionary에 key값이 있으면~
while True:
    cnt += 1 
    
    cur_x, cur_y = que.popleft()
    que.appendleft((cur_x,  cur_y))

    next_x = cur_x + dir[d][0]
    next_y = cur_y + dir[d][1]
    #벽에 박거나, 또는 자신의 몸에 닿는 경우!
    if(next_x <= 0 or next_x > n  or next_y <= 0 or next_y > n):
        break
    elif que.count((next_x, next_y)) >= 1:
        break

    #사과가 있다면...
    que.appendleft((next_x, next_y))

    if(board[next_x][next_y] == -1):
        board[next_x][next_y] = 0
    else:
        que.pop()


    #다음 이동할 곳이 방향을 바꿔야하는 시간이라면
    if cnt in change_dir:
        next_dir = change_dir[cnt]
        if(next_dir == 'D'):
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4


print(cnt)
