n = int(input())
distance = list(map(int,input().split()))
money = list(map(int,input().split()))

# 현재 비용이 다음보다 비싸면
# 현재 비용으로 한 구간만 이동하고
# 다음 비용을 현재 비용으로 업데이트 해주기

now = money[0]
total = 0


for i in range(n-1):
    if now > money[i]:
        now = money[i]
    total += now * distance[i]
print(total)

        
        

