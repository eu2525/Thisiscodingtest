a, b = map(int, input().split())

# Write your code here!
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

result = 0
for num in range(a, b + 1):
    if is_prime(num):
        result += num

print(result)