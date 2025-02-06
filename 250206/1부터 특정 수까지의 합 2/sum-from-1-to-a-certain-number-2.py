N = int(input())

# Write your code here!
result = 0
def gogo(n):
    global result
    if n == 1:
        result += n
        return
    
    result += n
    gogo(n - 1)

gogo(N)
print(result)