# 연속된 소수의 합으로 나타내는 자연수가 있음
# 41 = 2 + 3 + 5 + 7 + 11 + 13  or 11+13+17 or 41 => 3가지
# 연속된 이 중요함
# 7 + 13은 20이 되긴 하지만 7 13 사이에 11이 있어서 연속된 소수가 아님!!

# 소수 리스트를 구한다.
# 이중 for문으로 4000000까지의 소수들의 리스트를 구한다....??
# 아니였음 어떤 부분 수열에 대한 합인 경우에는 투포인터를 생각해보자!!

# 1) 소수 리스트를 구한다! -> 아리스토텔레스의 체? 인가 뭔가 이용
n = int(input())

is_prime = [False, False] + [True] * (n-1)
sosu_list = []

for i in range(2, n + 1):
    if is_prime[i]:
        sosu_list.append(i)
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False


# 2) 투 포인터를 이용한 연속된 소수 수열의 합을 구한다.
start = 0
end = 0
total = 0
cnt = 0

while True:
    if total == n:
        cnt += 1        
    if total > n:
        total -= sosu_list[start]
        start += 1
    elif end == len(sosu_list):
        break
    else:
        total += sosu_list[end]
        end += 1

print(cnt)


# # 이중 for문으로 다시 진행
# dp = [0] * (n + 1) 
# for idx, val in enumerate(sosu_list):
#     if val > n:
#         break
#     sum = 0
#     for k in range(idx, len(sosu_list)):
#         sum += sosu_list[k]
#         if sum > n:
#             break
#         else:
#             dp[sum] += 1

# print(dp[n])