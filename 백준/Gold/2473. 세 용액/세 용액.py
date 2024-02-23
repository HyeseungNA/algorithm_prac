n = int(input())
waters = list(map(int,input().split()))
waters.sort()
Min = 3000000000
result = []
for i in range(n):
    total = waters[i]
    tmp = waters[:i] + waters[i+1:]
    left = 0
    right = len(tmp) - 1
    while left < right:
        total = waters[i]
        total += tmp[left] + tmp[right]
        if abs(total) < abs(Min):
            Min = total
            result = [waters[i], tmp[left], tmp[right]]
            # print(total,result)

        if total == 0:
            break
        
        elif total < 0:
            left += 1
        
        else:
            right -= 1

result.sort()
print(*result)