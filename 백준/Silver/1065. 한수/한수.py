n = int(input())
cnt = 0
for num in range(1,n+1):
    num = str(num)
    flag = 1
    if len(num) <= 2:
        cnt += 1
        
    
    else:
        tmp = int(num[0]) - int(num[1])
        for i in range(1,len(num) - 1):
            if tmp != int(num[i]) - int(num[i+1]):
                flag = 0
                break
        if flag == 1:
            cnt += 1

print(cnt)