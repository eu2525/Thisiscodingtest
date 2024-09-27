import sys
sys.setrecursionlimit(100000)

T = int(input())

visited = []
team_list = []
result = 0
# 어느 프로젝트 팀에도 속하지 않는 학생들의 수
# 사이클 찾기

def find_cycle(st, team_mems):
    global visited, team_list, result
    visited[st] = True
    team_mems.append(st)
    next_pos = team_list[st - 1]

    if visited[next_pos]:
        if next_pos in team_mems:
            result += len(team_mems[team_mems.index(next_pos):])
    else:
        find_cycle(next_pos, team_mems)

for _ in range(T):
    N = int(input())
    visited = [False] * (N + 1)
    team_list = list(map(int,input().split()))
    for idx in range(len(team_list)):
        if not visited[idx]:
            team_mems = []
            find_cycle(idx,team_mems)
    print(N - result)
    result = 0