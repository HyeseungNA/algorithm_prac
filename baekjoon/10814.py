
n = int(input())
lst = []


# 인덱스 저장
for i in range(n):
    idx = i
    a,b = input().split()
    age = int(a)
    name = b
    lst.append([age,name,idx])

lst.sort(key=lambda x:(x[0],x[2]))

for i in range(n):
    print(int(lst[i][0]), lst[i][1])



'''
6
1 a
2 c
2 b
5 d
3 e
3 f

1 a
2 c
2 b
3 e
3 f
5 d
'''