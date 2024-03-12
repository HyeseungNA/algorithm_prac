num = int(input())
n = int(input())
if n > 0:
    bomb = list(map(int,input().split()))
else:
    bomb = []
Min = abs(num-100)

key = 0
while key <= 1000000:
    key_str = str(key)
    flag = 1
    for k in key_str:
        if int(k) in bomb:
            flag = 0
            break
    
    if flag == 1:
        Min = min(abs(key - num) + len(key_str),Min)
    key += 1
print(Min)

# import itertools

# tmp = [1,2,3,4]

# lst = list(itertools.product(tmp), repeat=)