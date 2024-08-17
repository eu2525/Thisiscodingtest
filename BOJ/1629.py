# A를 B번 곱한 수를 알고 싶다
# C로 나눠...
# 0.5초라서 반복문을 사용하는건 안됌!
# 규칙을 찾는 거 같은데....
# -> 규칙 찾는거 아니다! MergeSort처럼 하자!

a, b, c = map(int , input().split())

def divideandconquer(num, cnt):
    if cnt == 1:
        return (num % c)
            
    if cnt % 2 == 1:
        result = divideandconquer((num * num % c), (cnt - 1) / 2)
        result *= num
        return result % c
    else:
        result = divideandconquer((num * num % c) , cnt / 2)
        return result % c
        

print(divideandconquer(a,b))