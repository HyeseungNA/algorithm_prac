def dfs(now,cnt,sen):
    global Min,Max
    if cnt == len(compare):
        if Min == '':
            Min = sen
        else:
            Max = sen
        return
    
    if compare[cnt] == '<':
        for num in numbers:
            if num > now and visited[num]== 0:
                visited[num] = 1 
                dfs(num,cnt+1,sen+str(num))
                visited[num] = 0
             
    if compare[cnt] == '>':
        for num in numbers:
            if num < now and visited[num]== 0:
                visited[num] = 1           
                dfs(num,cnt+1,sen+str(num))
                visited[num] = 0
     



    
    


n = int(input())
compare = list(input().split())
numbers = [0,1,2,3,4,5,6,7,8,9]
visited = [0] * 10
Min = ''
Max = ''
for num in numbers:
    visited[num] = 1
    dfs(num,0,str(num))
    visited[num]= 0


print(Max)
print(Min)