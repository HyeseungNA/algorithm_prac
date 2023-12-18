import sys
input = sys.stdin.readline


def binary_search(target,start,end):
    mid = (start + end) // 2
    if start > end:
        return 0
    
    if numbers[mid] == target:
        return 1
    
    elif numbers[mid] > target:
        return binary_search(target, 0, mid - 1)

    else:
        return binary_search(target, mid + 1, end)





n = int(input())
numbers = list(map(int,input().split()))
m = int(input())
lst = list(map(int,input().split()))

numbers.sort()

for num in lst:
    print(binary_search(num, 0, len(numbers) - 1))