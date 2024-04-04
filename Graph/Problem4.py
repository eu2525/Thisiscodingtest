from collections import deque
import copy

n = int(input())

vec = [[] for _ in range(n + 1)]
cost = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    a = list(map(int, input().split()))
    en = i
    time = 0
    st = []
    for j in range(len(a)):
        if j == 0:
            time = a[0]
        else:
            if(a[j] == -1):
                continue
            else:
                st.append(a[j])

    cost[i] = time
    indegree[en] += len(st)
    for st_num in st:
        vec[st_num].append(en)

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

#이렇게 하면 복사가 안된다...ㅋ
#단순히 = 로 복사하는 경우에는 cost의 변화가 result에 반영됨.
#당연히 result의 결과도 cost에 변화를 줌.
#result = cost

#얕은 복사
#result = cost[:]

result = copy.deepcopy(cost)

while q:
    idx = q.popleft()
    for next in vec[idx]:
        indegree[next] -= 1
        result[next] = max(result[next], result[idx] + cost[next])
        if(indegree[next] == 0):
            q.append(next)

for idx in range(1, n+1):
    print(result[idx])