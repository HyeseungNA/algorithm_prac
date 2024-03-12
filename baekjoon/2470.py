def binary_search():
    global Min
    st = 0
    ed = len(waters) - 1
    answer = [waters[st],waters[ed]]
    
    

    while st < ed:
        total = waters[st] + waters[ed]
        if abs(total) < Min:
            Min = abs(total)
            answer = [waters[st], waters[ed]]


        if total == 0:
            return answer
        elif total > 0:
            ed -= 1
        else:
            st += 1
    return answer

n = int(input())
waters = list(map(int,input().split()))
waters.sort()
Min = 2000000000

result = binary_search()

result.sort()
for i in result:
    print(i,end = ' ')
'''
4
999999995 999999996 999999997 1000000000
'''