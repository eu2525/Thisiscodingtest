# 세 용액을 합쳐서 0에 가까운 용액을 만들어라
# 카테고리 이분탐색, 투포인터

n = int(input())
num_list = list(map(int,input().split()))

num_list.sort()

idx_1 = 0
idx_2 = 0
idx_3 = 0
result = 3e9

for idx in range(n - 2):
    current_num = num_list[idx]
    st = idx + 1
    en = n - 1
    while st < en:
        sum_num = current_num + num_list[st] + num_list[en]
        if abs(sum_num) < result:
            result = abs(sum_num)
            idx_1, idx_2, idx_3 = idx, st, en
        elif sum_num > 0:
            en -= 1
        else:
            st += 1

print(num_list[idx_1], num_list[idx_2], num_list[idx_3])