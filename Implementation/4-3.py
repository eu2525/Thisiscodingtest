cur = input()

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

#a를 0으로 어케 바꾸지....?
x = int(ord(cur[0])) - int(ord('a')) + 1
# ord(문자)
# 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
# ord('a') = 97
# chr(97) = 'a'
y = int(cur[1])

cnt = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8):
        cnt += 1

print(cnt)