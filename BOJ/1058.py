n = int(input())

graph = []

for _ in range(n):
    graph.append(list(input()))

f = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # 2-친구인 경우
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
                f[i][j] = 1

res = 0

for row in f:
    res = max(res,sum(row))
    
print(res)

# result = 0

# for i in range(n):
#     visited = [False] * n
#     visited[i] = True
#     for my_friend in friend_list[i]:
#         visited[my_friend] = True
#         for your_friend in friend_list[my_friend]:
#             if not visited[your_friend]:
#                 visited[your_friend] = True
    
#     result = max(result, sum(visited) - 1)

# print(result)
    