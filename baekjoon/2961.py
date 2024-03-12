def dfs(now,total,cnt,sin,seo):
    global Min
    sin *= ingredients[now][0]
    seo += ingredients[now][1]

    total = abs(sin-seo)
    
    Min = min(total, Min)
    if cnt == n:
        return
    
    for i in range(now+1,n):
        dfs(i,total,cnt+1,sin,seo)
    

n = int(input())
ingredients = []
Min = int(12e9)
for _ in range(n):
    a,b = map(int,input().split())
    ingredients.append([a,b])

for i in range(n):
    dfs(i,0,1,1,0)

print(Min)