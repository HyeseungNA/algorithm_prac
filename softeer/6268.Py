numbers = {
'': [],
'0':[0,1,2,4,5,6],
'1':[2,5],
'2':[0,2,3,4,6],
'3':[0,2,3,5,6],
'4':[1,2,3,5],
'5':[0,1,3,5,6],
'6':[0,1,3,4,5,6],
'7':[0,1,2,5],
'8':[0,1,2,3,4,5,6],
'9':[0,1,2,3,5,6]}

t = int(input())
for _ in range(t):
    cnt = 0
    num1, num2 = input().split()
    lst1 = [''] * (5 - len(num1))
    lst2 = [''] * (5 - len(num2))
    lst1.extend(num1)
    lst2.extend(num2)

    for i in range(5):
        if lst1[i] == lst2[i]:
            continue
        for num in numbers[lst1[i]]:
            if num not in numbers[lst2[i]]:
                cnt += 1
        
        for num in numbers[lst2[i]]:
            if num not in numbers[lst1[i]]:
                cnt += 1
    
    print(cnt)


'''
2
1 2
9881 10724
'''
    