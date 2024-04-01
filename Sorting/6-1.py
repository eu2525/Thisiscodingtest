array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    # array swap을 통해서 ㅓ두 변수의 위치를 변경할 수 있음.
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)