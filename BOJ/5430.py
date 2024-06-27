# 2가지 함수 R , D
# R : 배열에 있는 수의 순서를 뒤집는 함수
# D : 첫번째 수를 버리는 함수 -> 배열이 비어있는 경우 D 사용시 에러 발생

# t : test_case 수
t = int(input())

for _ in range(t):
    command = input()
    length = int(input())
    num_list = input()
    if length == 0:
        num_list = []
    else:
        num_list = num_list[1:-1]
        num_list = list(map(int, num_list.split(",")))
    
    errors = False
    rr = 0
    for idx in range(len(command)):
        com = command[idx]
        if com == "R":
            rr +=1
        else:
            if(len(num_list) <= 0):
                errors = True 
                break
            else:
                if rr % 2 == 0:
                    num_list.remove(num_list[0])
                else:
                    num_list.pop()

    if(errors == False):
        if rr % 2 == 1:
            num_list = list(reversed(num_list))
        print('[', end='')
        print(*num_list, sep=',', end='')
        print(']')
    else:
        print("error")