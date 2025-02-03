n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_num = -1
# Write your code here!
# 직사각형의 크기를 구하기
for row_ck in range(1, n + 1):
    for col_ck in range(1, m + 1):
        for r in range(n - row_ck + 1):
            for c in range(m - col_ck + 1):
                # (r,c)가 시작점
                find_square = True
                for r_idx in range(row_ck):
                    for c_idx in range(col_ck):
                        if not find_square:
                            break

                        if grid[r + r_idx][c + c_idx] <= 0:
                            find_square = False
                
                if find_square:
                    max_num = max(max_num, row_ck * col_ck)

print(max_num)
                    