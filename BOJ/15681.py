n, root_num, q = map(int,input().split())

tree = [[] for _ in range(n + 1)]

visit = [-1] * (n+1)

for _ in range(n - 1):
    st, en = map(int,input().split())
    tree[st].append(en)
    tree[en].append(st)

def dfs(now):
    global visit
    visit[now]=1
    for i in tree[now]:
        if visit[i]== -1:
            visit[now]+=dfs(i) 
    return visit[now] 

dfs(root_num)

for _ in range(q):
    t = int(input())
    print(visit[t])