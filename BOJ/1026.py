n = int(input())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

a_list.sort()
result = 0

for i in range(len(a_list)):
    result += a_list[i] * max(b_list)
    b_list.remove(max(b_list))
    
print(result)    
