import math
n = int(input())
arr = [True] * (n+1)
arr[0]= False
arr[1] = False
prime_num = []
for i in range(2,int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while (i * j) <= n:
            arr[i*j] = False
            j += 1
for i in range(2,n+1):
    if arr[i] == True:
        prime_num.append(i)

total =0
left = 0
right = 0
cnt = 0

while True:
    if total < n:
        if right == len(prime_num):
            break
        else:
            total += prime_num[right]
            right += 1
    else:
        if total == n:
            cnt += 1
        total -= prime_num[left]
        left += 1

print(cnt)
    

