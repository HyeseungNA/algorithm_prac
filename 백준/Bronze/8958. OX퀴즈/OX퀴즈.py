n = int(input())


for _ in range(n):
    cnt = 0
    total = 0
    scores = list(input())
    for score in scores:
        if score == 'O':
            cnt += 1
        else:
            cnt = 0
        total += cnt
    print(total)