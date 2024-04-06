#완전탐색으로 풀어야할듯?
def solution(s):
    answer = len(s)
    for length in range(1, int(len(s)/ 2) + 1):
        new_str = ''
        idx = 0 
        # python str은 범위를 넘어가도 되더라
        # ex) n = "123" print(n[1:10000]) 이래도 "23"이 출력.
        while idx < len(s):
            base = s[idx : idx + length]
            cnt = 1
            
            while base == s[idx + length * cnt : idx + length * (1+cnt)]:
                cnt += 1
                
            if cnt == 1:
                new_str += base
                idx += length 
            else:
                new_str += (str(cnt) + base)
                idx += length * cnt
        
        
        answer = min(answer, len(new_str))
            
    return answer