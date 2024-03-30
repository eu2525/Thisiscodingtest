from collections import deque

#Python에서는 deque를 이용해 queue 자료구조 이용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
print(queue)
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
