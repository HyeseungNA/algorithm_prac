while True:
    try:
        legos = []
        x = int(input()) * 10 ** 7
        n = int(input())
        for _ in range(n):
            legos.append(int(input()))
        legos.sort()
        left = 0
        right = n - 1
        total = 0
        flag = 0
        while left < right:
            total = legos[left] + legos[right]
            # print(total,left,right)
            if total == x:
                flag = 1
                break
            
            elif total > x:
                right -= 1
            
            else:
                left += 1
        if flag == 1:
            print(f'yes {legos[left]} {legos[right]}')
        else:
            print('danger')
    except:
        break