n,l = map(int,input().split())
waters = list(map(int,input().split()))

waters.sort()
cnt = 0
st = waters[0] - 0.5
ed = st + l
cnt = 1
for water in waters:
    if st <= water - 0.5 and water + 0.5 <= ed:
        continue

    else:
        st = water - 0.5
        ed = st + l
        cnt += 1


print(cnt)
