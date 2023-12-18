t = int(input())
for _ in range(t):
    n = int(input())
    cnt =  1
    scores = [list(map(int,input().split())) for _ in range(n)]

    scores = sorted(scores,key=lambda x: x[0])

    top = 0

    for i in range(1,n):
        if scores[i][1] < scores[top][1]:
            top = i
            cnt += 1
        
    print(cnt)

    
