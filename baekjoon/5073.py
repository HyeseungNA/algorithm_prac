


while True:
    lst = list(map(int,input().split()))
    # 다 000이면 멈춰
    if lst.count(0) == 3:
        break
    # 그게 아니라면
    else:
        lst.sort()
        if lst[2] >= lst[0] + lst[1]:
            print('Invalid')
        else:
            # 세 변이 같을 때
            if len(set(lst)) == 1:
                print('Equilateral')

            # 두 변이 같을 떄
            elif len(set(lst)) == 2:
                print('Isosceles')

            # 세 변이 다를 때
            else:
                print('Scalene')
