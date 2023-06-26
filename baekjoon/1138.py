n = int(input())
numbers = list(map(int,input().split()))

tmp = [0] * n
cnt = 0 # 자신보다 큰 사람

for i in range(n):
    cnt = 0
    for j in range(n):
        # cnt랑 numbers랑 같고, tmp에 비어져 있으면 넣기!
        if cnt == numbers[i] and tmp[j] == 0:
            tmp[j] = i + 1
            break
        if tmp[j] == 0:
            cnt += 1

print(*tmp)