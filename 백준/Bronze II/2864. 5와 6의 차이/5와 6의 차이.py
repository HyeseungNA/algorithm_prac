num1, num2 = input().split()
Min = 0
Max = 0

num1 = num1.replace('6','5')
num2 = num2.replace('6','5')

Min = int(num1) + int(num2)


num1 = num1.replace('5','6')
num2 = num2.replace('5','6')

Max = int(num1) + int(num2)
print(Min,Max)