n,st,ed = map(int,input().split())
cnt = 0
while st != ed:
    st -= st // 2
    ed -= ed // 2
    cnt += 1
print(cnt)