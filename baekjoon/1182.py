n,s = map(int,input().split())
lst = list(map(int,input().split()))
answer = 0
# s랑 같으면 개수 더해주기
def dfs(level,total):
    global answer
    
    if level == n:
        if total == s:
            answer += 1
        return
    
    dfs(level + 1, total + lst[level])
    dfs(level + 1, total)

dfs(0,0)
if s == 0:
    print(answer-1)
else:
    print(answer)

