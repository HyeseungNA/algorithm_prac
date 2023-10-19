n,m = map(int,input().split())
clouds = [list(input()) for _ in range(n)]



# 구름을 0으로 만들어주기
for i in range(n):
    for j in range(m):
        if clouds[i][j] == 'c':
            clouds[i][j] = 0

# print(clouds)
# 구름이동 표시하기
for i in range(n):
    for j in range(1,m):
        # 전에 구름이었으면 cnt 해주기
        if clouds[i][j-1] != '.':
            if clouds[i][j] == 0:
                continue
            else:
                clouds[i][j] = clouds[i][j-1] + 1

for i in range(n):
    for j in range(m):
        if clouds[i][j] == '.':
            clouds[i][j] = -1


for i in range(n):
    print(*clouds[i])