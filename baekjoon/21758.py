n = int(input())
honey = list(map(int,input().split()))
lst = [] # 꿀 최대값을 담는 곳
total = sum(honey)
answer = 0

# 벌 - 벌 - 꿀
tmp = honey[0]
for i in range(1,n):
    tmp += honey[i]
    answer = max(answer, total - honey[0] - honey[i] + total - tmp)


honey.reverse()
# 꿀 - 벌 - 벌
tmp = honey[0]
for i in range(1,n):
    tmp += honey[i]
    answer = max(answer, total - honey[0] - honey[i] + total - tmp)



# 벌 - 꿀 - 벌
for i in range(1,n):
    answer = max(answer,total - honey[0] - honey[-1] + honey[i])

  

print(answer)