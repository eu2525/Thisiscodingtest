# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다. 
# 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 
T = int(input())

for _ in range(T):
    n, m = map(int,input().split())
    data = list(map(int,input().split()))
    
    result = 1
    while data:
        # list에 제일 앞에 값보다 하나라도 큰 값이 있으면!!
        if data[0] < max(data):
            data.append(data.pop(0))
        elif m == 0:
            break
        else:
            data.pop(0)
            result += 1

        if m > 0:
            m -= 1
        else:
            m = len(data) - 1

    print(result)
