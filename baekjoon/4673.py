create_num = [0] * (10001)
for num in range(1,10001):
    tmp = num
    while num > 0: 
        num,na = divmod(num,10)
        tmp += na
    
    if tmp <= 10000:
        create_num[tmp] += 1
    


for i in range(1,10001):
    if create_num[i] == 0:
        print(i)