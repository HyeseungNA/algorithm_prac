from itertools import combinations_with_replacement
n,m = map(int,input().split())

numbers = list(map(int,input().split()))
numbers.sort()
result = list(combinations_with_replacement(numbers,m))

for re in result:
    print(*re)