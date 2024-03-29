array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start,end):
    if start >= end:
        return 
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        while right > start and array[right] >= array[pivot]:
            right -= 1
        