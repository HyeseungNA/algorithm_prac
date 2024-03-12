cnt = 1
while True:
    result = 0
    l,p,v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        break
    
    n,na = divmod(v,p)
    if na > l:
        result = n * l + l
    else:
        result = n * l + na
    print(f'Case {cnt}: {result}')
    cnt += 1