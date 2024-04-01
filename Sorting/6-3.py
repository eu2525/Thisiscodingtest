#QuickSort
array = [5,7,9,0,3,1,6,2,4,8]

def partition(low, high):
    global array
    pivot = low
    left = low + 1
    right = high
    while(left <= right):
        while left <= high and array[left] <= array[pivot]:
            left += 1
        while right > low and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right] , array[pivot] = array[pivot] , array[right]    
        else:
            array[left] , array[right] = array[right] , array[left]

    return right

def quicksort(low, high):
    if(high > low):
        pivot = partition(low,high)
        quicksort(low, pivot-1)
        quicksort(pivot+1,high)

print(array)
quicksort(0, len(array) - 1)
print(array)