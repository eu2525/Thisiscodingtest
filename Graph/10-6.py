#위상 정렬
from collections import deque
v, e = map(int, input().split())

vec = [[] for _ in range(v+1)]
indegree = [0] * (v + 1)

for _ in range(e):
    st, en = map(int, input().split())
    indegree[en] += 1
    vec[st].append(en)

que = deque()

for i in range(1, v + 1):
    if(indegree[i] == 0):
        que.append(i)

while que:
    idx = que.popleft()
    print(idx, end = ' ')
    for i in vec[idx]:
        indegree[i] -= 1
        if(indegree[i] == 0):
            que.append(i)
        
