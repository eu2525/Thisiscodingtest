from collections import deque

n , m = map(int,input().split())

q = deque()

for idx in range(1, n + 1):
    q.append(idx)

num = list(map(int,input().split()))

cnt = 0
for id in num:
    #q.index(10) -> deque에서 10이 위치한 index를 반환.
    #list.index(100) -> 도 리스트 안에 100의 값의 위치를 반환.
    # 중복되는 원소들의 인덱스 모두 찾기 (numpy.where)
    # numpy.where(b == 'hello')[0]
    # array([1, 3])
    id_idx = q.index(id)
    mid = len(q) / 2
    if(id_idx < mid):
        while(q[0] != id):
            q.rotate(-1)
            cnt +=1
    else:
        while(q[0] != id):
            q.rotate(1)
            cnt += 1
    q.popleft()


print(cnt)