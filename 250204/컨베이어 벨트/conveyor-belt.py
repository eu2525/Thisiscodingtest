n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Write your code here!
for _ in range(t):
    next_d = [d[-1]]
    next_u = [u[-1]]
  
    new_u = u[:-1]
    new_d = d[:-1]
    next_d.extend(new_u)
    next_u.extend(new_d)

    d = next_d
    u = next_u

for j in d:
    print(j, end = ' ')
print()
for i in u:
    print(i, end = ' ')
