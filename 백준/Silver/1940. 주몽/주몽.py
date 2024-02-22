n = int(input())
m = int(input())
clothes = list(map(int,input().split()))
clothes.sort()

left = 0
right = len(clothes) - 1
cnt = 0
while left < right:
    total = clothes[left] + clothes[right]
    if total == m:
        cnt += 1
        left += 1
        right -= 1
    
    elif total < m:
        left += 1
    else:
        right -= 1
    
print(cnt)