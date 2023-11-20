n = int(input())
orders = list(input().split())

x = 1
y = 1


for order in orders:
    if order == 'L':
        x -= 1  
        # 범위를 넘어서면 다시 원상복구
        if x < 1:
            x += 1
    
    if order == 'R':
        x += 1
        if x > n:
            x -= 1
    
    if order == 'U':
        y -= 1
        if y < 1:
            y += 1

    if order == 'D':
        y += 1
        if y > n:
            y -= 1

print(y, x)
