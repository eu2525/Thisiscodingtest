import sys
from heapq import heappush, heappop

heap_list = []

n = int(sys.stdin.readline())

for _ in range(n):
    input_num = int(sys.stdin.readline())
    
    if input_num == 0:
        if(len(heap_list) == 0):
            print(0)
        else:
            print(heappop(heap_list)[1])
    else:
        heappush(heap_list, (abs(input_num), input_num))