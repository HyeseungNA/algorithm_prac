from bisect import bisect_left


n,h = map(int,input().split())

Min = float('inf')

down = []
up = []

for i in range(n):
    if i % 2 == 0:
        up.append(int(input()))
    
    else:
        down.append(int(input()))

up.sort() # 작은 순서부터
down.sort()
cnt = 0 
for i in range(1,h+1):
    cntUp = bisect_left(up,i)
    cntdown = bisect_left(down, h+1-i)
    total = n - (cntUp + cntdown)
    if Min > total:
        Min = total
        cnt = 1
    elif Min == total:
        cnt += 1
print(Min, cnt)