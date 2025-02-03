n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
# Write your code here!
for j in range(n - 2):
    for i in range(n - 2):
        # i, j 가 이제 시작점임.
        cnt = 0
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                if grid[row][col] == 1:
                    cnt += 1

            max_cnt = max(max_cnt, cnt)

print(max_cnt)