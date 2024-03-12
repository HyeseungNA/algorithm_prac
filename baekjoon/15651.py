from itertools import product
n,m = map(int,input().split())

numbers = [i for i in range(1,n+1)]

arr = list(product(numbers, repeat = m))

for ar in arr:
    ar = list(ar)
    print(*ar)