from collections import Counter

n = int(input())
cards = list(map(int,input().split()))
m = int(input())
com = list(map(int,input().split()))

c = dict(Counter(cards))

for num in com:
    if num in c:
        print(c[num],end = ' ')
    else:
        print(0, end = ' ')
