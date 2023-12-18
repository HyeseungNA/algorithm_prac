import sys
input = sys.stdin.readline

def find(x):

    if x != parents[x]:
        parents[x]= find(parents[x])
    return parents[x]

def union(x,y):

    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    if x > y:
        parents[x] = y

n,m = map(int,input().split())
parents = [0] * (n+1)
cycle = False
for i in range(1,n+1):
    parents[i] = i

for i in range(m):
    a,b = map(int,input().split())
    if find(a) == find(b):
        print(i+1)
        cycle = True
        break
    else:
        union(a,b)

if cycle == False:
    print(0)