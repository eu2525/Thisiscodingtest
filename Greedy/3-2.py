n,m,k = map(int,input().split())
num = list(map(int,input().split()))

num.sort(reverse = True)

count = int(m / (k+1)) * k
count += m % (k+1) 

result = 0
result += count * num[0]
result += (m - count) * num[1]

print(result)


# 아래의 경우 M이 매우 커진다면 시간 초과가 날 수 있음.
'''
while(True):
    for i in range(k):
        if m == 0:
            break
        result += num[0]
        m -= 1
    if m == 0:
        break
    result += num[1]
    m -= 1

print(result)
'''