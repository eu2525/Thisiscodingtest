import sys
sys.setrecursionlimit(10**6)

n = int(input())
nodes_length = [[] for _ in range(n + 1)]
max_one_leaf = [0] * (n + 1)

result = 0

for _ in range(n-1):
    # 부모 노드, 자식 노드 , 가중치
    pr, ch, w = map(int,input().split())
    nodes_length[pr].append((ch, w))

def dfs(idx):
    global result, max_one_leaf
    edge_list = [] 
    for node_num, w in nodes_length[idx]:
        dfs(node_num)
        edge = max_one_leaf[node_num] + w
        edge_list.append(edge)
    edge_list.sort(reverse = True)
    if len(edge_list) == 1:
        max_one_leaf[idx] = max_one_leaf[nodes_length[idx][0][0]] + nodes_length[idx][0][1]
        result = max(result, max_one_leaf[idx])
    elif len(edge_list) >= 2:
        result = max(result, edge_list[0] + edge_list[1])
        max_one_leaf[idx] = edge_list[0]

dfs(1)

print(result)