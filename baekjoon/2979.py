a,b,c = map(int,input().split())
lst = [0] * 101
for _ in range(3):
    # 동시에 있는 경우들 구하기
    st,ed = map(int,input().split())
    for i in range(st,ed):
        lst[i] += 1

total = lst.count(1) * a + (lst.count(2) * 2) * b + (lst.count(3) * 3) * c


print(total)