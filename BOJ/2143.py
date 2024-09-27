import bisect

T = int(input())
n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int,input().split()))

# 모든 연속된 누적합을 모으는 리스트를 생성 
# ex) [1, 3, 1, 2] -> [1, 4, 5, 7, 3, 4, 6, 1, 3, 2]
sum_a_list, sum_b_list = [], []
for i in range(n):
    for j in range(i+1, n+1):
        sum_a_list.append(sum(a_list[i:j]))
for i in range(m):
    for j in range(i + 1, m + 1):
        sum_b_list.append(sum(b_list[i:j]))

# 누적합 리스트를 정렬
sum_a_list.sort()
sum_b_list.sort()

# [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6]
# 누적합 리스트가 위와 같이 정렬되었으므로 bisect로 해당하는 숫자의 갯수를 세어줌
result = 0
for i in range(len(sum_b_list)):
    target_num = T-sum_b_list[i]
    left_idx = bisect.bisect_left(sum_a_list, target_num)
    right_idx = bisect.bisect_right(sum_a_list, target_num)
    result += (right_idx-left_idx)

print(result)