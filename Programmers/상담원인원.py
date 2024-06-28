# 멘토 n명, 상담 유형 1~k
# 멘토는 자신이 담당하는 유형의 상담만 가능
# 멘토는 참가자 한 명과만 상담 가능,
# 상담 시간은 참가자 요청 시간 만큼 소요

# 상담 규칙
# 1. 참가자 상담 유형을 담당하는 멘토 중 상담이 아닌 멘토에게 배정
# 2. 해당 유형의 멘토가 모두 상담중 -> 기다림
# 2-1. 기다림의 시간은 참가자 상담 요청 ~ 상담 시작까지의 시간
# 3. 상담 종료 후 기다리는 인원이 있으면 바로 상담 시작
# 3-1. 상담 먼저 요청한 참가자 우선

# 기다린 시간의 합이 최소가 되도록 멘토 인원 결정
from heapq import heappush, heappop
from itertools import combinations_with_replacement, permutations

def cal_waiting_time(waiting_list , mento_num):  
    end_time = []
    wait_time = 0
    for st_time, sp_time in waiting_list:
        if mento_num > 0:
            heappush(end_time, st_time + sp_time)
            mento_num -= 1
        else:
            cur_time = heappop(end_time)
            if cur_time > st_time:
                wait_time += cur_time - st_time
                heappush(end_time, cur_time + sp_time)
            else:
                heappush(end_time, st_time + sp_time)
            
    return wait_time

def solution(k, n, reqs):
    
    waiting_list = [[] for _ in range(k)]
    
    for req in reqs:
        waiting_list[req[2] - 1].append([req[0], req[1]])
    
    #몰랐던 부분
    cases = set()
    for comb in combinations_with_replacement([i for i in range(1, n - k + 2)], r=k):
        if sum(comb) == n:
            for perm in permutations(comb, k):
                cases.add(perm)
                
    result = 1e9
    for case in cases:
        time = 0
        for i in range(k):
            time += cal_waiting_time(waiting_list[i], case[i])
        result = min(result, time)
            
    return result