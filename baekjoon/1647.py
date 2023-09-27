# 크루스칼 알고리즘,,,
import sys
input = sys.stdin.readline


# 부모 찾아주기
def find(num):
    if parent[num] != num:
        p = find(parent[num])
        parent[num] = p
    
    return parent[num]

def union(a,b):
    
    # # 부모가 같지 않으면 합쳐주기
    # a = find(a)
    # b = find(b)

    if a == b:
        return
    
    if a < b:
        parent[b] = a
    
    else:
        parent[a]  = b


n,m = map(int,input().split())
parent = [0] * (n+1)
lst = [list(map(int,input().split())) for _ in range(m)]
lst.sort(key=lambda x:x[2])
# print(lst)

for i in range(n+1):
    parent[i] = i

result = 0

for i in range(m):
    # 부모가 다르면 연결해주기
    r_a = find(lst[i][0])
    r_b = find(lst[i][1])
    cost = lst[i][2]
    if r_a != r_b:
        union(r_a,r_b)
        result += cost
        end = lst[i][2]


print(result - end)

