def dfs(left,right,top,bottom,color):
    global Min
    if color == k+1:
        Min = min(Min, (right-left) * (top - bottom))
        return 
    
    for point in colors[color]:
        x = point[0]
        y = point[1]

        Nleft = min(left, x)
        Nright = max(right,x)
        Ntop = max(top,y)
        Nbottom = min(bottom,y)
        if Min > (Nright - Nleft) * (Ntop - Nbottom):
            dfs(Nleft,Nright,Ntop,Nbottom,color+1)


n,k = map(int,input().split())
colors = [[] for _ in range(k+1)]
for _ in range(n):
    point = list(map(int,input().split()))
    colors[point[2]].append(point[:2])

Min = 2000 * 2000
dfs(1000,-1000,-1000,1000,1)
print(Min)