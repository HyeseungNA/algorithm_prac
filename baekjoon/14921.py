n = int(input())
waters = list(map(int,input().split()))
left = 0
right = n - 1
result = int(1e9)
while left < right:
    total = waters[left] + waters[right]
    
    if total < 0:
        if abs(total) < abs(result):
            result = total
        left += 1
    elif total == 0:
        result = 0
        break
    else:
        if abs(total) < abs(result):
            result = total
        right -= 1

print(result)

'''
6
-7 -4 -1 1 2 6
'''