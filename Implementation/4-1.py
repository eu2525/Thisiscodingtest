n = int(input())
direction = list(map(str, input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
move_types = ['R','L','U','D']


x = 1
y = 1

for dir in direction:
    for i in range(len(move_types)):
        if dir == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if(nx >= 1 and nx <= n and ny >= 1 and ny <= n):
        x, y = nx, ny

print(x, y)