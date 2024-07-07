n = int(input())

meeting_schedule = []

for _ in range(n):
    st_t, en_t = map(int,input().split())
    meeting_schedule.append((st_t, en_t))

meeting_schedule.sort(key = lambda x: (x[1], x[0]))

start_end_time = -999
result = 0

for st, en in meeting_schedule:
    if st >= start_end_time:
        start_end_time = en
        result += 1

print(result)