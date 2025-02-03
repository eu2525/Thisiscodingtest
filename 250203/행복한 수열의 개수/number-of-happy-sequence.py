# n * n 크기의 격자 정보가 주어짐
# 행복한 수열 : 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
# 행 + 열 해서 2n개 중에 행복한 수열의 개수 세기

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
# 행복한 수열을 세는 방법
result = 0

# 행을 보는 경우
for row in range(n):
    prev_num = grid[row][0]
    cnt = 1
    for j in range(1, n):
        if grid[row][j] != prev_num:
            prev_num = grid[row][j]
            cnt = 1
        else:
            cnt += 1
        
        if cnt >= m:
            result += 1
            break
        


# 열을 보는 경우
for col in range(n):
    prev_num = grid[0][col]
    cnt = 1
    for i in range(1, n):
        if grid[i][col] != prev_num:
            prev_num = grid[i][col]
            cnt = 1
        else:
            cnt += 1
        
        if cnt >= m:
            result += 1
            break

print(result)