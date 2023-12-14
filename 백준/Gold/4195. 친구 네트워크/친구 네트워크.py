import sys
input = sys.stdin.readline
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        visited[x] += visited[y]

t = int(input())
for _ in range(t):
    n = int(input())
    parent = {}
    visited = {}
    for _ in range(n):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            visited[a] = 1
    
        if b not in parent:
            parent[b] = b
            visited[b] = 1
    
        union(a,b)
        print(visited[find(a)])