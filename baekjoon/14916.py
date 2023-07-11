money = int(input())
cnt = 0

while money >0:
    # 5로 나누어 떨어지면 몫을 더해준다
    if money % 5 == 0:
        cnt += money // 5
        break
    # 2원씩 준다
    else:
        money -= 2
        cnt += 1

if money < 0:
    cnt = -1

print(cnt)

