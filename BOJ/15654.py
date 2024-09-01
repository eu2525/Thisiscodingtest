n , m = map(int, input().split())
input_num_list = list(map(int, input().split()))

input_num_list.sort()

visited = [False] * n
result_graph = []

def bfs():
    if len(result_graph) == m:
        print(' '.join(map(str,result_graph)))
    
    for idx, num in enumerate(input_num_list):
        if visited[idx]:
            continue

        visited[idx] = True
        result_graph.append(num)
        bfs()
        visited[idx] = False
        result_graph.pop()

bfs()