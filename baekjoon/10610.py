num = list(input())

if '0' not in num:
    print(-1)
else:
    total = 0
    for n in num:
        total += int(n)
    if total % 3 == 0:
        num.sort(reverse=True)
        print(int(''.join(num)))
    else:
        print(-1)
    


