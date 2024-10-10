import bisect

n = int(input())
num_list = list(map(int,input().split()))

result = [num_list[0]]

for item in num_list:
    if result[-1] < item:
        result.append(item)
    else:
        push_idx = bisect.bisect_left(result, item)
        result[push_idx] = item

print(len(result))