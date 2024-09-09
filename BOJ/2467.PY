# 산성, 아칼리성 용액을 보유
# -1000000000~1000000000 범위
# 산성은 양수 알칼리성은 음수
# 두 용액을 섞어서 0에 가깝게 만들기
# 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.


n = int(input())
num_list = list(map(int,input().split()))

min_val = 2e9
answer = [float('inf'), float('inf')]
left, right = 0, n-1

while left < right:
    if abs(num_list[left] + num_list[right]) < min_val:
        min_val = abs(num_list[left] + num_list[right])
        answer = [num_list[left], num_list[right]]
    # 음수이면 양수쪽으로 이동
    if num_list[left] + num_list[right] < 0:
        left += 1
    # 합이 양수이면 음수쪽으로 이동
    else:
        right -= 1

print(*answer)




'''
n = int(input())
num_list = list(map(int,input().split()))
sorted_list = []

for num in num_list:
    if num < 0:
        sorted_list.append((-1 * num, -1))
    else:
        sorted_list.append((num,1))

start_num, start_pm = sorted_list[0]
result_a , result_b = 0, 0
result = 2000000000

for i in range(1, len(sorted_list)):
    prev_num, prev_pm = sorted_list[i]
    current_num = start_num * start_pm + prev_num * prev_pm
    if abs(current_num) < abs(result):
        result = current_num
        result_a = start_num * start_pm
        result_b = prev_num * prev_pm

    start_num,start_pm = prev_num, prev_pm

print(min(result_a, result_b), max(result_a, result_b))
'''
