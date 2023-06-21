n,k = map(int,input().split())
numbers = list(map(int,input().split()))

# 총 합을 미리 계산

# 앞에꺼 추가해주고 뒤에꺼 빼주기

total = sum(numbers[:k])
lst = [total]
for i in range(k,n):
    total += numbers[i] - numbers[i-k]
    lst.append(total)

print(max(lst))
    
