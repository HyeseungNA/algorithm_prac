n,l = map(int,input().split())
waters = list(map(int,input().split()))
waters.sort()
start = waters[0]
cnt = 1
for water in waters[1:]:
    if (water + 0.5) - (start - 0.5) <= l:
        continue
    else:
        cnt += 1
        start = water
print(cnt)