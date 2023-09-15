n = int(input())
for _ in range(n):
    cnt = 0
    childrens = list(map(int,input().split()))
    for i in range(1,len(childrens)-1):
        for j in range(i+1,len(childrens)):
            if childrens[i] > childrens[j]:
                childrens[i],childrens[j] = childrens[j],childrens[i]
                cnt += 1
            
    print(childrens[0],cnt)