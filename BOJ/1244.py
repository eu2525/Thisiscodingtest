n = int(input())
switches = list(map(int, input().split()))
i = int(input())

for _ in range(i):
    s, j = map(int, input().split())
    j = j - 1
    if s == 1:
        for idx in range(j, n, j + 1):
            switches[idx] = (switches[idx] + 1) % 2 
    else:
        idx = 1
        while(j + idx < n and j - idx >= 0):
            if switches[j + idx] == switches[j - idx]:
                idx += 1
            else:
                break
        switches[j] = (switches[j] + 1) % 2
        for cg_cnt in range(1, idx):
            switches[j + cg_cnt] = (switches[j + cg_cnt] + 1) % 2
            switches[j - cg_cnt] = (switches[j - cg_cnt] + 1) % 2

for num in range(n):
    if num % 20 == 19:
        print(switches[num])
    else:
        print(switches[num], end = ' ')
