n = int(input())
lope = []

for i in range(n):
    weight = int(input())
    lope.append(weight)

lope.sort(reverse=True)

j = 0
Max = 0
while j < n:
    total = 0
    total = lope[j] * (j + 1)
    if Max <= total:
        Max = total
    
    j += 1

print(Max)