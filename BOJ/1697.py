from collections import deque

def bfs(v, target):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        #만약 que에서 나오는게 도착지이면~
        if v == target:
            return array[v]
        #For문을 통해서 다음 정보를 넣음!
        for next_v in (v-1, v+1, 2*v):
            # next_v가 범위 안에 있고, 이전에 들어간 값이 없다면~
            if 0 <= next_v < MAX and array[next_v] == 0:
                array[next_v] = array[v] + 1
                q.append(next_v)


MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX
print(bfs(n, k))


'''
# 처음에 내가 푼 풀이 -> DP식 접근...
n, k = map(int, input().split())

time_list = [100001] * 200001

time_list[n] = 0

for i in range(k+1):
    time_list[i] = min(abs(n-i), min(time_list[i], min(time_list[i-1] + 1, time_list[i+1] + 1)))
    time_list[2*i] = min(time_list[i] + 1, time_list[2*i])

print(time_list[k])
'''