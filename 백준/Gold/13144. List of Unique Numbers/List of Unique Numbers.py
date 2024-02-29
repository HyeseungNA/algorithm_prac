n = int(input())
numbers = list(map(int,input().split()))
vistited = [0] * (100001)

left = 0
right = 0
result = 0
while left <= right and right < n:
    if vistited[numbers[right]] == 0:
        vistited[numbers[right]] = 1
        right += 1
        result += (right - left)
    
    else:
        vistited[numbers[left]] = 0
        left +=1

print(result)