from collections import deque
import itertools
import copy
n = int(input())
numbers = list(map(int,input().split()))
counts = list(map(int,input().split()))
tmp = ['+','-','*','%']
types = []
Max = int(-1e9)
Min = int(1e9)


for i in range(4):
    types.extend([tmp[i]] * counts[i])


types_lst = list(set(itertools.permutations(types,len(types))))
for types in types_lst:
    types = deque(types) # 가능한 순열을 데큐로 만들어주기
    numbers_copy = copy.deepcopy(numbers)
    numbers_copy = deque(numbers_copy)
        
    num1 = numbers_copy.popleft()
    while types and numbers_copy:
        num2 = numbers_copy.popleft()
        type = types.popleft()
        # print(num1,num2,type,'🌹')
        if type == '+':
            num1 = num1 + num2

        if type == '-':
            num1 = num1 - num2
            
        if type == '*':
            num1 = num1 * num2
            
        if type == '%':
            if num1 < 0 and num2 > 0:
                num1 = (abs(num1) // num2) * -1
            else:
                num1 = num1 // num2
    
        
    #     print(num1,num2,'🌸')   
    # print(num1,'🤍')    
    Max = max(Max,num1)
    Min = min(Min,num1)

print(Max)
print(Min)
            










