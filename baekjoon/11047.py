n,k = map(int,input().split())
moneys = []
cnt = 0
for _ in range(n):
    moneys.append(int(input()))

# 돈을 큰 순서로 정렬시킴
moneys.sort(reverse=True)

for i in range(n):
    while True:

        if k - moneys[i] >= 0:
            k -= moneys[i]
            cnt += 1
        
        else:
            break
print(cnt)


    

