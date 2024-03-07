from itertools import combinations_with_replacement

n,m = map(int,input().split())
numbers = [i for i in range(1,n+1)]

arr = list(combinations_with_replacement(numbers,m))
arr.sort()

for a in arr:
    a = list(a)
    a.sort()
    print(*a)
    