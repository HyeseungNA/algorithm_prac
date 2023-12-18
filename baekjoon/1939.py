n , m = map(int,input().split())
parent = [[] for _ in range(n+1)]

print(parent)
for i in range(n+1):
    parent[i].append([i,0])



for _ in range(m):
    a,b,c = map(int,input().split())


st,ed = map(int,input().split())