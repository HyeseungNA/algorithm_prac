from collections import defaultdict
n = int(input())
cnt = 0
for _ in range(n):
    order = input()
    if order == 'ENTER':
        d = defaultdict(int) # enter일 때마다 새로운 딕셔너리 생성
        
    else:
        if order not in d:
            d[order] += 1
            cnt += 1

print(cnt)
    