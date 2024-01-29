n = input()
f = int(input())
result = 0

num = int(n[:-2] + '00')
while True:
    if num % f == 0:
        result = str(num)
        break
    num += 1



print(result[-2:].zfill(2))
'''
270
3
'''