def binary_seacrh(now):
    global result
    st = 1
    ed = house[-1] - house[0]

    while st <= ed:
        cnt = 1
        mid = (st + ed) // 2
        current = house[0]
        for i in range(1,n):
            if house[i] - current >= mid:
                cnt += 1
                current = house[i]

        if cnt >= now:
            result = max(mid,result)
            st = mid + 1
        else:
            ed = mid - 1
    return


n,c = map(int,input().split())
house = []
result = 0
for _ in range(n):
    house.append(int(input()))

house.sort()

binary_seacrh(c)
print(result)