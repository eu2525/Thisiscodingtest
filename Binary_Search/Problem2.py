n = int(input())
store = list(map(int,input().split()))
m = int(input())
want = list(map(int,input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2
    
    if(array[mid] == target):
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)



store.sort()
  
for idx in want:
    if binary_search(store, idx, 0, n - 1) == True:
        print("yes" , end = ' ')
    else:
        print("no", end = ' ')

# in 함수를 통해서 있는지 확인할 수도 있음.
# list에는 find 함수 말고 in 함수 이용!
for idx in want:
    if idx in store:
        print("yes" , end = ' ')
    else:
        print("no", end = ' ')