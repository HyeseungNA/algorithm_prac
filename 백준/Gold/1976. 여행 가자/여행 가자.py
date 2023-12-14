def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(y, x):
    y = find(y)
    x = find(x)

    if y < x:
        parents[x] = y
    else:
        parents[y] = x

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
plans = list(map(int, input().split()))
parents = [i for i in range(n + 1)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i + 1, j + 1)  # 노드 번호는 1부터 시작하므로 인덱스에 1을 더해줍니다.

for i in range(1, m):
    if find(plans[i]) != find(plans[0]):
        print('NO')
        break
else:
    print('YES')
