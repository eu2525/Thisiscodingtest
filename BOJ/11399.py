n = int(input())

wait_time = list(map(int,input().split()))

wait_time.sort()

result = 0
for i in range(1, n + 1):
    result += sum(wait_time[0:i])
    #result += (wait_time[i] * (len(wait_time) - i))

print(result)