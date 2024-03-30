stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
print(stack)
stack.append(1)
stack.append(4)
stack.pop()

print(stack)

print(stack[::-1])

# [::-1]은 리스트의 슬라이싱(slicing)을 이용하여 역순으로 리스트를 가져오는 구문. 
# 슬라이싱은 [start:stop:step] 형태로 사용.
# 따라서 [::-1]은 전체 리스트를 역순으로 가져오라는 의미.
