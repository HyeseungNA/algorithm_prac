t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    Alst = list(map(int,input().split()))
    Blst = list(map(int,input().split()))
    cnt = 0
    st = a - 1
    ed = 0
    Alst.sort()
    Blst.sort(reverse=True)

    while st >= 0 and ed < b:
        if Alst[st] > Blst[ed]:
            cnt += (b - ed)
            st -= 1

        else:
            ed += 1
    print(cnt)
    