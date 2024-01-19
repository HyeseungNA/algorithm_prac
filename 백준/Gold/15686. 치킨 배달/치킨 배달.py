def dfs(chickens):
    result = 0
    for i in range(n):
        for j in range(n):
            if Map[i][j] == 1:
                Min = int(1e9)
                distance = 0
                h_x= j
                h_y = i
                for y,x in chickens:
                    distance = abs(x - h_x) + abs(y- h_y)
                    Min = min(Min,distance)
                
                result += Min

    return result



import itertools

n,m = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(n)]
chickens = []
result = int(1e9)

for i in range(n):
    for j in range(n):
        if Map[i][j] == 2:
            chickens.append([i,j])

chicken = list(itertools.combinations(chickens,m))
for chick in chicken:
    answer = dfs(chick)
    result = min(answer,result)

print(result)


