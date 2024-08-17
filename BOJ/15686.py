n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

chicken_info = []
house_info = []
for row in range(n):
    for col in range(n):
        if graph[row][col] == 1:
            house_info.append((row,col))
        elif graph[row][col] == 2:
            chicken_info.append((row,col))

select_chicken_house = []
result = 50 * 50

def dfs(next_idx, select_list):
    global result
    if len(select_list) == m:
        list_distance = 0
        for home_r, home_c in house_info:
            min_distance = 50*50
            for select_row, select_col in select_list:
                min_distance = min(min_distance, abs(home_r - select_row) + abs(home_c - select_col))
            list_distance += min_distance
        result = min(result, list_distance)
    else:
        for idx, (chicken_row, chicken_col) in enumerate(chicken_info):
            if idx < next_idx:
                continue
            else:
                select_list.append((chicken_row, chicken_col))
                dfs(idx+1, select_list)
                select_list.pop()
                dfs(idx+1, select_list)
    
dfs(0, select_chicken_house)

print(result)

