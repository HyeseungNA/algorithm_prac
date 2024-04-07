import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int,input().split()))
b,c = map(int,input().split())
cnt = 0
for student in students:
    student -= b
    cnt += 1
    if student > 0:
        if student % c == 0:
            cnt += (student // c)
        else:
            cnt += (student //c) + 1
print(cnt)
