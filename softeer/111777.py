import sys
input = sys.stdin.readline

n =  int(input())
hous = list(map(int,input().split()))
Max= 0
for pie in range(2,max(hous)+ 1):
    cnt = 0
    for h in hous:
        if h % pie == 0:
            cnt += 1
    Max = max(Max, cnt)

print(Max)