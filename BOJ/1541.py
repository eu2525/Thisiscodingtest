dis = input()
dis = dis.split('-')

# 괄호를 적절히 쳐서 식의 최소값을 만듬
# +, - 로만 이루어짐!
result = 0
if dis[0].find('+'):
    plus_dis = dis[0].split('+')
    num = 0
    for i in range(len(plus_dis)):
        num += int(plus_dis[i])
    result += num
else:
    result = dis[0]


for idx in range(1, len(dis)):
    if dis[idx].find('+'):
        plus_dis = dis[idx].split('+')
        num = 0
        for i in range(len(plus_dis)):
            num += int(plus_dis[i])
        result -= num
    else:
        result -= int(dis[idx])

print(result)