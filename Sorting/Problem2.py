N = int(input())

array = []

for i in range(N):
    num = int(input())
    array.append(num)

array.sort(reverse = True)
# result = sorted(array, reverse = True)

print(array)