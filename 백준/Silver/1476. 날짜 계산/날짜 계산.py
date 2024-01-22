e,s,m = map(int,input().split())

st_e,st_s,st_m = 0,0,0
cnt = 0
while True:
    if st_e == e and st_s == s and st_m == m:
        print(cnt)
        break

    st_e = (st_e + 1) % 15
    if st_e == 0:
        st_e = 15
    st_s = (st_s + 1) % 28
    if st_s == 0:
        st_s= 28
    st_m = (st_m + 1) % 19
    if st_m == 0:
        st_m = 19

    cnt += 1