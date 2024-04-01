n = int(input())

array = []
for i in range(n):
    #Python에서 제공하는 split 함수를 이용하여 입력받는다.
    #문자열.split()을 통해 list로 return 한다.
    input_data = input().split() #list
    array.append((input_data[0], input_data[1]))

#split 과 map 함수를 활용하여 숫자를 다중으로 입력받는다.
#map 함수는 map ( [적용할 함수], [적용할 값] ) 으로 활용할 수 있다.


# key를 이용하여 점수를 기준으로 정렬
array = sorted(array, key =lambda student : student[1])

print(array)

'''
exam_score = {}

for _ in range(n):
    # 홍길동 95
    name, score = map(str, input().split())
    exam_score[name] = int(score)

result = sorted(exam_score, key = lambda x : exam_score[x])

print(result)
'''