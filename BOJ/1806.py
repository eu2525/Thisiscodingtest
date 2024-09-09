n, s = map(int,input().split())
num_list = list(map(int, input().split()))

start, end = 0, 0
result = start
min_length = 1e9

while True:
    # 만약 총 합이 S가 넘는다면, start를 하나씩 옮겨보면서 어디까지 길이가 줄어드나 확인
    if result >= s:
        min_length = min(min_length, end - start)
        result -= num_list[start]
        start += 1
    elif end == n:
        break
    else:
        result += num_list[end]
        end += 1

if min_length == 1e9:
    print(0)
else:
    print(min_length)