import itertools

n,m = map(int,input().split())
lst = list(map(int,input().split()))
cards = list(itertools.combinations(lst,3))
Max = 0
for card in cards:
    if sum(card) <= m:
        Max = max(sum(card),Max)
    

print(Max)