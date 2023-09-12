# dp 인가?
# 1 : 1
# 2 ~ 7  : 6
# 8 ~ 19 : 12
# 20 ~ 37 : 18 
# 38 ~ 61 : 24

n = int(input())
cnt = 1
bee = 1


while True:
    if n <= bee:
        break
    else:
        bee += (6 * cnt)
        cnt += 1


print(cnt)
