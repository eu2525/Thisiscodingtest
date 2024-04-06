n = input()

mid = len(n) // 2

l_sum = 0
r_sum = 0

left = n[:mid]
right = n[mid:]

for i in range(len(left)):
    l_sum += int(left[i])

for i in range(len(right)):
    r_sum += int(right[i])

if l_sum == r_sum:
    print("LUCKY")
else:
    print("READY")