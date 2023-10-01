def dfs(cnt,ch):

    if cnt == k:
        if ch not in result:
            result.append(ch)

    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            dfs(cnt+1,ch+lst[i])
            v[i] = 0

    return result


# 결과물 담을 리스트

n = int(input())
k = int(input())
lst = []

for _ in range(n):
    lst.append(input())

# 결과물 담을 리스트
result = []

v = [0] * (n+1)

dfs(0,'') # 깊이, 결과물

print(len(result))