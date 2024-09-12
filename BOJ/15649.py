n, m = map(int,input().split())


result_list = []

def dfs():
    global result_list
    if len(result_list) == m:
        print(' '.join(map(str, result_list)))
    else:
        for idx in range(1, n+1):
            if idx in result_list:
                continue
            result_list.append(idx)
            dfs()
            result_list.pop()

dfs()