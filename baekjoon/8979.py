n,k = map(int,input().split())
score = [0] * (n + 1)

com = [list(map(int,input().split())) for _ in range(n)]


com.sort(key=lambda x: (x[1],x[2],x[3]), reverse=True)

score = [1] * (n+1)
idx = [com[i][0] for i in range(n)].index(k)

for i in range(n):
    if com[idx][1:] == com[i][1:]:
        print(i+1)
        break

