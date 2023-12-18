n = int(input())
bag = 0

while n > 0:
    if n % 5 == 0:
        n -= 5
        bag += 1
    else:
        n -= 3
        bag += 1

if n < 0:
    print(-1)
else:
    print(bag)