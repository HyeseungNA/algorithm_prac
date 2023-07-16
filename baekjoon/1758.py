n = int(input())
money = []
for _ in range(n):
    money.append(int(input()))

money.sort(reverse=True)
total = 0

for i in range(n):
    if money[i] - i < 0:
        continue
    total += money[i] - i
    
print(total)