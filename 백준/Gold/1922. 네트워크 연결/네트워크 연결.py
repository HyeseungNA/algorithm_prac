def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a,b):

    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    elif a > b:
        parents[a] = b

n = int(input())
m = int(input())
edges = []
parents = [0] * (n+1)
result = 0

for i in range(n+1):
    parents[i] = i

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append([cost,a,b])

edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find(a) != find(b):
        union(a,b)
        result += cost
print(result)