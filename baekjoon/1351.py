from collections import defaultdict

def dfs(n):
    if n in d:
        return d[n]
    else:
        d[n] = dfs(n//p) + dfs(n//q)
        return d[n]

n,p,q = map(int,input().split())
d = defaultdict(int)
d[0] = 1
print(dfs(n))