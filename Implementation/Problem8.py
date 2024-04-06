n = input()

result = []
num = 0
#문자열을 for x in n 이런식으로 하나씩 볼수도 있네...
for x in n:
    if x.isalpha(): #str.isalpha() -> alpha인지 보는거래요. 처음에는 A <= x and x <= Z로 함.
        result.append(x)
    else:
        num += int(x)

result.sort()

for abc in result:
    print(abc , end = '')
print(num)