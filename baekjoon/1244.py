def change(num):
    if switch[num] == 1:
        switch[num] = 0
    else:
        switch[num] = 1

n = int(input())
switch = [-2] + list(map(int, input().split()))
m = int(input())  # 학생 수

for _ in range(m):
    gender, number = map(int, input().split())

    # 남자일 때
    if gender == 1:
        # 배수들 다 바꿔주기
        for i in range(number,n+1,number):
            change(i)
    
    # 여자일 때
    if gender == 2:
        change(number)
        for j in range(1, n//2):
            if number + j > n or number - j < 1:
                break
            if switch[number + j] == switch[number -j]:
                change(number+j)
                change(number-j)
            else:
                break

# 스위치 상태 출력
for i in range(1, n + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
