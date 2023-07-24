numbers = list(input().split('-'))
total = 0

for num1 in numbers[0].split('+'):
    total += int(num1)

for num2 in numbers[1:]:
    for n2 in num2.split('+'):
        total -= int(n2)

print(total)
