n = int(input())
wave = [300,60,10]
answer = []
for w in wave:
    cnt = 0
    cnt = n // w
    answer.append(cnt)
    n -= (w * cnt)

if n == 0:
    print(*answer)

else:
    print(-1)
