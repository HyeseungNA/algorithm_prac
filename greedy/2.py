n,m = map(int,input().split())
cards = [list(map(int,input().split())) for _ in range(n)]

cards[0].sort()

result = cards[0][0]

for i in range(1,n):
    # 카드 정렬
    cards[i].sort()
    # 처음 수보다 크면 답 바꿔주기
    if cards[i][0] > result:
        result = cards[i][0]
    else:
        continue

print(result)
   