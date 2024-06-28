# t1 ~ t2 사이의 온도 조절
# 희망온도 설정 -> 중간에 변경 가능한 값

# 에어컨 on 
    # 실내온도 != 희망온도 : 실내 온도 -> 희망 온도로 1분에 1도 이동
    # 실내온도 == 희망온도 : 동일하게 유지
# 에어컨 off 
    # 실내온도 != 실외온도 : 실내 온도 -> 실외 온도로 1분에 1도 이동
    # 실내온도 == 실외온도 : 변화 X

# 소비전력
    # 에어컨 on
        # 희망온도  != 실내온도 : a만큼 소비
        # 같다면 : b만큼 소비
    # 에어컨 off
        # 전력 소모 X
        
# dp[i][j]
    # i : 시간
    # j : 온도
    # 저장되는 값 : 비용
    
# temp방향과 온도 방향을 정하자!
    
def calc_temp(dp, time, cur_temp, t1, t2, a, b, direction, temperature):
    calc_temperature = 1e9
    # 온도를 높일 때 에어컨을 ON (겨울 느낌)
    if direction == True:
        if cur_temp >= t1 + 10 and cur_temp <= t2 + 10:
            calc_temperature = min(dp[time - 1][cur_temp] + b, min(dp[time - 1][cur_temp -1] + a, dp[time - 1][cur_temp + 1]))
        else:
            if cur_temp == temperature:
                calc_temperature = min(dp[time - 1][cur_temp - 1], min(dp[time - 1][cur_temp], dp[time - 1][cur_temp + 1]))
            elif cur_temp < temperature:
                calc_temperature = dp[time-1][cur_temp - 1]
            else:
                calc_temperature = min(dp[time - 1][cur_temp - 1] + a, dp[time - 1][cur_temp + 1])  
    # 온도를 낮출 때 에어컨을 ON (여름 느낌)
    else:   
        if cur_temp >= t1 + 10 and cur_temp <= t2 + 10:
            calc_temperature = min(dp[time - 1][cur_temp] + b, min(dp[time - 1][cur_temp + 1] + a, dp[time - 1][cur_temp - 1]))
        else:
            if cur_temp == temperature:
                calc_temperature = min(dp[time - 1][cur_temp + 1] , min(dp[time - 1][cur_temp], dp[time - 1][cur_temp - 1]))
            elif cur_temp > temperature:
                calc_temperature = dp[time-1][cur_temp + 1]
            else:
                calc_temperature = min(dp[time - 1][cur_temp + 1] + a, dp[time - 1][cur_temp - 1]) 

    return calc_temperature

def solution(temperature, t1, t2, a, b, onboard):
    
    answer = 1e9
    dp = [[1e9] * 52 for _ in range(len(onboard) + 1)]

    
    # False 이면 온도가 낮출때 에어컨을 켜야함 (여름)
    # True 이면 온도를 높일 때 에에컨을 켜야함 (겨울)    
    direction = temperature < (t1 + t2) / 2
    
    for time, value in enumerate(onboard):
        if time == 0:
            dp[0][temperature + 10] = 0
        else:
            for temp in range(51):
                if value == 1:
                    if temp >= t1 + 10 and temp <= t2 + 10:
                        dp[time][temp] = calc_temp(dp, time, temp, t1, t2, a, b, direction, temperature + 10)
                    else:
                        dp[time][temp] = 1e9
                else:
                    dp[time][temp] = calc_temp(dp, time, temp, t1, t2, a, b, direction, temperature + 10)
                    
    for i in range(51):
        answer = min(answer, dp[len(onboard) - 1][i])

    return answer