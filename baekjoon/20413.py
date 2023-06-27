n = int(input())
moneys = list(map(int,input().split()))
grade = list(input())

# 게임에 쓴 총합 
total = 0
money = 0


for i in range(len(grade)):
    # 브론즈 가기 위한 돈
    if grade[i] == 'B':
        money = moneys[0] - 1 - money

    # 실버 가기 위한 돈
    elif grade[i] == 'S':
        money = moneys[1] - 1 - money



    # 골드 가기 위한 돈
    elif grade[i] == 'G':
        money = moneys[2] -1 - money
 

    # 플래티넘 가기 위한 돈
    elif grade[i] == 'P':
        money = moneys[3] -1 - money
     

    # 다이어몬드 가기 위한 돈
    elif grade[i] == 'D':
        money = moneys[3]
    total += money
print(total)

