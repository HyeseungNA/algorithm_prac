import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 0이면 두 개 합치기
# 1이면 부모루트 확인하기

def find(num):
    if parent[num] == num:
        return num
    
    else:
        p = find(parent[num])
        parent[num] = p
        return parent[num]


def union(a,b):

    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if a < b:
        parent[b] = a
    
    elif a > b:
        parent[a] = b


m,n = map(int,input().split())
parent = [0] * (m+1)
for i in range(m+1):
    parent[i] = i

for i in range(n):
    order,a,b = map(int,input().split())
    

    if order == 0:
        union(a,b) # 부모 합칩시돠

    elif order == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')