import copy,sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(n)]
Min = 256
Max = 0
Min_sec = int(12e9)
result = []
for i in range(n):
    Max = max(Max,max(Map[i]))
    Min = min(Min,min(Map[i]))

for height in range(Min,Max+1):
    sec = 0
    take_block = 0
    use_block = 0
    for i in range(n):
        for j in range(m):
            if height < Map[i][j]: # 블록이 더 많을 때
                take_block += Map[i][j] - height
                
            else:
                use_block = height - Map[i][j]
    
    if use_block - take_block > b:
        continue
    else:
        sec = take_block * 2 + use_block
        Min_sec = min(Min_sec,sec)
        result = height


print(Min_sec,result)