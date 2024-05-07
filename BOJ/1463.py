n = int(input())

cnt = [0,0,1]

for i in range(3, n+1):
    cnt.append(9999999)
    if i % 3 == 0:
        cnt[i] = min(cnt[i // 3] + 1, cnt[i])

    if i % 2 == 0:
        cnt[i] = min(cnt[i // 2] + 1, cnt[i])
    
    cnt[i] = min(cnt[i - 1] + 1, cnt[i])

print(cnt[n])