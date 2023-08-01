def dfs(color,left,right,bottom,top):
    global minArea
    if color == k+1:
            minArea = min(minArea, (right-left) * (top - bottom))
            return
    for point in colors[color]:
        x,y = point[0],point[1]
        leftN,rightN = min(left,x), max(right,x)
        bottomN,topN = min(bottom,y), max(top,y)
        dfs(color+1,leftN,rightN,bottomN,topN)


n,k = map(int,input().split())
colors = [[] for _ in range(k+1)]
for _ in range(n):
    point = list(map(int,input().split()))
    colors[point[2]].append(point[:2])

minArea = 2000 * 2000
dfs(1,1000,-1000,1000,-1000)

'''
5 2
-4 -2 1
-5 -3 1
5 -4 2
4 -5 2
3 -8 2
'''
print(minArea)