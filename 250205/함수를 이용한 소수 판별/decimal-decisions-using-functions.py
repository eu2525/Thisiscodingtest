a, b = map(int, input().split())

# Write your code here!

sosu_list = [False] * 201

def is_prime(a):    
    for idx in range(2 * a, 100, a):
        sosu_list[idx] = True


for i in range(2, 100):
    is_prime(i)

result = 0
for num in range(a, b + 1):
    if sosu_list[num] == False:
        result += num

print(result)