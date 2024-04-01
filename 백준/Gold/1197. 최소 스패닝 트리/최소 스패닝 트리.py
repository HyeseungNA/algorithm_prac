
v,e = map(int,input().split())
edges = []
root = {}

for i in range(1,v+1):
    root[i]= i


def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(a,b):
    A = find(a)
    B = find(b)

    if A > B:
        root[A] = B

    else:
        root[B] = A  

for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append([a,b,c])

edges.sort(key=lambda x:x[2])
total = 0


for a ,b, cost in edges:
    if find(a) == find(b):
        continue

    else:
        total += cost
        union(a,b)

print(total)