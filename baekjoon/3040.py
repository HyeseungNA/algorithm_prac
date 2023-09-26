def comb(now,cnt):
    if cnt == 7:
        if sum(total) == 100:
            for t in total:
                print(t)
        
    
    for i in range(now,9):
        total.append(lst[i])
        comb(i+1,cnt + 1)
        total.pop()







lst = []
total = []
for _ in range(9):
    lst.append(int(input()))


# 조합으로 풀어야징,,아오 하기싫어

comb(0,0)