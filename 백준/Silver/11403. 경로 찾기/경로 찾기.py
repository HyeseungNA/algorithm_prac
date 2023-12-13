n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[j][i] and arr[i][k]:
                arr[j][k] = 1

for a in arr:
    print(*a)
