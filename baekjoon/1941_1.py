from collections import deque
def bfs(si,sj):
    q = deque()
    v2 = [[0] * 5 for _ in range(5)]
    q.append((si,sj))
    v2[si][sj] = 1
    cnt = 1

    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and v2[ni][nj] == 0 and v1[ni][nj] == 1:
                q.append((ni,nj))
                v2[ni][nj] = 1
                cnt += 1

    if cnt == 7:
        return True
    

def check():
    for i in range(5):
        for j in range(5):
            if v1[i][j] == 1:
                return bfs(i,j)


def dfs(n,cnt,scnt):
    global ans
    if cnt > 7:
        return
    if n == 25:
        if cnt == 7 and scnt >=4:
                if check():
                    ans += 1
        return

    v1[n//5][n%5] = 1
    dfs(n+1,cnt+1, scnt+int(arr[n//5][n%5]=='S'))
    v1[n//5][n%5] = 0
    dfs(n+1,cnt,scnt)
arr = [input() for _ in range(5)]
ans = 0
v1 = [[0]  * 5 for _ in range(5)]
# 학ㅇ번호, 포함학생수, 다솜파
dfs(0,0,0)
print(ans)