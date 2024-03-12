n = int(input())
numbers = [i for i in range(1,n+1)]
left = 0
right = 0
total = numbers[left]
cnt = 0
while right <= n and left <= right:
    if total == n:
        right += 1
        cnt += 1
        if right < n:
            total += numbers[right]
        else:
            break
        
    
    elif total < n:
        right += 1
        total += numbers[right]
    
    else:
        total -= numbers[left]
        left += 1

print(cnt)