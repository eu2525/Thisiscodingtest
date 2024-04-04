n, m = map(int, input().split())

team = [0] * (n+1)

def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a != b:
        team[a] = b

#team 초기화
for i in range(1, n + 1):
    team[i] = i

for _ in range(m):
    num, a, b= map(int, input().split())
    if num == 0:
        union_team(team, a, b)
    elif num == 1:
        team_a = find_team(team, a)
        team_b = find_team(team, b)
        if team_a != team_b:
            print("NO")
        else:
            print("YES")