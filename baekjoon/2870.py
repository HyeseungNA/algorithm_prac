n = int(input())
nums = ['0','1','2','3','4','5','6','7','8','9']
result = []
for _ in range(n):
    lst = input()
    tmp = ''
    for i in lst:
        if i in nums:
            tmp += i
        else:
            if tmp:
                result.append(int(tmp))
                tmp = ''
    if tmp:
        result.append(int(tmp))

result.sort()
for n in result:
    print(n)



