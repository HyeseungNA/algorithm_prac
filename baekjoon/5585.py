n = int(input())
coines = [500,100,50,10,5,1]

money = 1000 - n
cnt = 0

for coin in coines:
    cnt += money // coin
    money -= (money // coin) * coin


print(cnt)