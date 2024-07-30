n, m = map(int, input().split())
result_list = []

def dfs(start):
    if len(result_list) < m:
        for idx in range(start, n + 1):
            result_list.append(idx)
            dfs(idx)
            result_list.pop()
    else:
        for num in result_list:
            print(num , end = " ")
        print()
    
dfs(1)