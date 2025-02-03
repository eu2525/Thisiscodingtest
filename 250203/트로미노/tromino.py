n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_num = 0 
# Write your code here!
# 사각형에서 하나씩 뺀거
for i in range(n - 1):
    for j in range(m - 1):
        square_sum = grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i + 1][j + 1]
        for row in range(i, i + 2):
            for col in range(j, j + 2):
                max_num = max(max_num, square_sum - grid[row][col])
        
# 3개 일렬로 한거
# 가로 합
for i in range(n):
    for j in range(m - 2):
        max_num = max(max_num, sum(grid[i][j : j + 3]))

# 세로 합
for j in range(m):
    for i in range(n - 2):
        max_num = max(max_num, grid[i][j] + grid[i + 1][j] + grid[i + 2][j])

print(max_num)
