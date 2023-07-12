n,m = map(int,input().split())
j = int(input())
left = 1
right = m
cnt = 0

for i in range(j):
    apple = int(input())
    if left <= apple <= right:
        continue

    elif right < apple:
        cnt += apple - right
        left += (apple - right)
        right = apple
        
    
    elif left > apple:
        cnt += left - apple
        right -= (left - apple)
        left = apple
        

print(cnt)
    
