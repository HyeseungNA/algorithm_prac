
def check(y,x):
    for i in range(y,y+3):
        for j in range(x,x+3):
            A[i][j] =  1 - A[i][j]


n,m = map(int,input().split())
A = [list(map(int,input())) for _ in range(n)]
B = [list(map(int,input())) for _ in range(n)]
cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            cnt += 1
            check(i,j)

flag = 0


if (n < 3 or m < 3) and A !=B:
    flag = 1
    

else:
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                flag = 1
                break
        if flag == 1:
            break

if flag == 1:
    print(-1)
else:
    print(cnt)