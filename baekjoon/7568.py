n = int(input())

body = [list(map(int,input().split())) for _ in range(n)]

score = []

for i in range(n):
    cnt = 1
    for j in range(n):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            cnt += 1
    
    score.append(cnt)

print(*score)