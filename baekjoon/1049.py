n,m = map(int,input().split())
prices = []
for _ in range(m):
    price = 0
    prices.append(list(map(int,input().split())))

packages = sorted(prices,key=lambda x:x[0])
ones = sorted(prices, key=lambda x:x[1])

packages_price = packages[0][0]
ones_price = ones[0][1]
packages_cnt = 0
one_cnt = 0 

if packages_price > ones_price * 6:
    price = ones_price * n
else:
    if packages_price > (n % 6) * ones_price: # 나머지 비교 낱개가 더 쌀 때
        packages_cnt = n // 6
        one_cnt = n - (packages_cnt * 6)
        price = packages_cnt * packages_price + one_cnt * ones_price
    else:
        if n % 6 == 0:
            packages_cnt = n // 6
            price = packages_price * packages_cnt
        else:
            packages_cnt = (n // 6) + 1
            price = packages_price * packages_cnt
print(price)
                
            

 