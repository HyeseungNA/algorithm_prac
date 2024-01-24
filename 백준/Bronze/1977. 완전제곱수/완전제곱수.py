import math
a = int(input())
b = int(input())

lst = []
aa = math.sqrt(a)
bb = math.sqrt(b)

for num in range(a,b+1):
    if int(math.sqrt(num)) == math.sqrt(num):
        lst.append(num)


if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)