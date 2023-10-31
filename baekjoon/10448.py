t = int(input())
num = []
for i in range(1,46):
    num.append(i*(i+1)/2)
    
for _ in range(t):
    n = int(input())
    flag = 0
    for i in num:
        for j in num:
            for k in num:
                if i + j + k == n:
                    flag =1
                if i + j + k > n:
                    break 
    
    print(flag)