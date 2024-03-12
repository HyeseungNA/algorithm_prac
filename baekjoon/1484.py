g = int(input())


left = 1
right = 2
result = []
while left < right:
    diff = (right ** 2) - (left ** 2)
    if diff == g:
        result.append(right)
        right += 1
        left += 1
    
    elif diff < g:
        right += 1
    
    else:
        left += 1

    
if result:
    print(*result,sep='\n')
else:
    print(-1)
    