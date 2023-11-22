n = int(input())
charge = [25,10,5,1]

for _ in range(n):
    money = int(input())
    
    for c in charge:
        print(money // c,end = ' ')
        money = money % c

    

    