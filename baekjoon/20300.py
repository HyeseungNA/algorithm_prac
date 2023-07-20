n = int(input())
machine = list(map(int,input().split()))

# 정렬하기
machine.sort()



# 짝수일떄
Max = 0
if len(machine) % 2 == 0:
    for i in range(n//2):
        if Max < machine[i] + machine[n-1-i]:
            Max = machine[i] + machine[n-1-i]
    print(Max)

# 홀수일때
if n % 2 == 1:
    Max2 = machine[-1]
    for i in range((n-1)//2):
        if Max2 < machine[i] + machine[n-2-i]:
            Max2 = machine[i] + machine[n-2-i]

    print(Max2)
