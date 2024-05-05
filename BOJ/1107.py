n = int(input())
m = int(input())

if(m != 0):
    broken_key = list(map(int, input().split()))
else:
    broken_key = []

def gotokey(num, broken_key):
    found = True
    for k in broken_key:
        if str(k) in str(num):
            found = False
            break
        
    return found

button = [500001] * 1000002

button[100] = 0
cnt = 0
while (button[n] >= cnt):
    if(n - cnt >= 0):
        if(button[n-cnt] == 500001 and gotokey(n-cnt, broken_key)):
            button[n-cnt] = len(str(n-cnt))
        button[n] = min(button[n], button[n-cnt] + cnt)
    if(n+cnt < 1000002):
        if(gotokey(n+cnt, broken_key) and button[n+cnt] == 500001):
            button[n+cnt] = len(str(n+cnt))
        button[n] = min(button[n], button[n+cnt] + cnt)
    cnt += 1

print(button[n])