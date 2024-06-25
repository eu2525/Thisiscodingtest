from collections import deque

n = int(input())
students = deque(map(int,input().split()))

stack = []
idx = 1
while students:
    # Stack이랑 비교하는 경우
    if stack and stack[-1] == idx:
        stack.pop()
        idx += 1 
        continue
    # Queue랑 비교하는 경우
    std_num = students.popleft()
    if std_num != idx:
        stack.append(std_num)
    else:
        idx += 1

found = False
# Queue가 끝나고 Stack의 숫자가 오름차순인지 확인
while stack:
    stk_num = stack.pop()
    if idx != stk_num:
        found = True
        break
    else:
        idx += 1

# Stack에 남아 있는게 없거나, 오름차순으로 잘 정렬된 경우는 Nice
if(found == False):
    print("Nice")
# 아닌 경우는 Sad를 출력
else:
    print("Sad")
