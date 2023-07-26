num = input()
Min = ''
Max = ''

cnt = 0
for n in num:
    if n == 'M':
        cnt += 1
    else:
        if cnt > 0:
            Max += str(5 * (10 ** cnt))
            Min += str((10 ** cnt) + 5)
        else:
            Max += '5'
            Min += '5'
        cnt = 0


if cnt > 0:
    Min += str(10 ** (cnt-1))
    Max += '1' * cnt
print(Max)
print(Min)