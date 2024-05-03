t = int(input())

fibo = [(1,0), (0,1)]

idx = 2
while(idx <= 40):
    p1_0, p1_1 = fibo[idx - 1]
    p2_0, p2_1 = fibo[idx - 2]
    fibo.append((p1_0+p2_0, p1_1+p2_1 ))
    idx += 1

for _ in range(t):
    a = int(input())
    print(fibo[a][0], fibo[a][1])