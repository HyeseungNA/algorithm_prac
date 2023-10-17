n,num,p = map(int,input().split())

if n == 0:
    print(1)
else:
    lst = list(map(int,input().split()))
    # 등수 
    ranking = {}
    lst.append(num)
    # 점수 내림차순 정렬
    lst.sort(reverse=True)
    ranking[lst[0]] = 1
    
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            continue
        else:
            ranking[lst[i]] = i + 1

    
    if len(lst) > p and lst[-1] == num:
        print(-1)
    else:
        print(ranking[num])
    
