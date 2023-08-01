def pick(cnt,start):
    global lst
    # cnt가 7이면 return
    if cnt == 7:
        if sum(lst) == 100:
            for i in sorted(lst):
                print(i)
            exit()
        return
    # total이 100이면 난쟁이 출력해주고 멈추기
    for i in range(start,9):
        # 난쟁이 넣어주고
        lst.append(dwarfs[i])
        # 다음 난쟁이 넣어주고
        pick(cnt+1,i+1)
        lst.pop()



dwarfs = list(int(input()) for _ in range(9))
lst = []
pick(0,0)