import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))


# 부모 채워주기
def dfs(x,depth):
    c[x] = True
    d[x] = depth

    for y in lst[x]:
        if c[y]:
            continue
        p[y] = x
        dfs(y,depth+1)

def lca(st,ed):

    # 깊이 같게
    while d[st] != d[ed]:

        if d[st] > d[ed]:
            st = p[st]

        else:
            ed = p[ed]

    while st != ed:
        st = p[st]
        ed = p[ed]
    return st

n = int(input())
lst = [[] for _ in range(n+1)]
c = [0] * (n+1)
d = [0] * (n+1)
p = [0] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    lst[b].append(a)
    lst[a].append(b)

dfs(1,0)

m = int(input())
for _ in range(m):
    st,ed = map(int,input().split())
    print(lca(st,ed))

