from collections import deque

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))
    result = [0] * (n + 1)
    graph = [[] * (n + 1) for _ in range(n + 1)]
    building = [0] * (n + 1)

    for _ in range(k):
        st, en = map(int, input().split())
        graph[st].append(en)
        building[en] += 1

    w = int(input())
  
    que = deque()

    for idx in range(1, n + 1):
        if building[idx] == 0:
            que.append((idx, cost[idx - 1]))
            result[idx] = cost[idx - 1]

    while que:
        st_idx, idx_cost = que.popleft()
        for next_idx in graph[st_idx]:
            building[next_idx] -= 1
            
            if idx_cost + cost[next_idx - 1] > result[next_idx]:
                result[next_idx] = idx_cost + cost[next_idx - 1]
              
            if building[next_idx] == 0:
                que.append((next_idx, result[next_idx]))

    print(result[w])
