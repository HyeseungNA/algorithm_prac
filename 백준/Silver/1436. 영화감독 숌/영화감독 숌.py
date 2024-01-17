n = int(input())

num = 666
cnt = 0 
while True:
    com = str(num)
    if '666' in com:
        cnt += 1
        if cnt == n:
            print(num)
            break
    
    num += 1