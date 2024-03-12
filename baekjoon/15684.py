import sys
def check():
    for i in range(n):
        tmp = i
        for j in range(h):
            if ladder[j][tmp] == 1:
                tmp += 1
            
            elif tmp > 0 and ladder[j][tmp-1] == 1:
                tmp -= 1
        
        if tmp != i:
            return False
    
    return True


def dfs(x,y,cnt):
    global ans
    if cnt >= ans:
        return
    
    if check():
        ans = cnt
        return
    
    if cnt == 3:
        return
    

    for i in range(y,h):
        if i == y:
            now = x
        else:
            now = 0
        for j in range(now,n-1):
            if ladder[i][j] == 0:
                ladder[i][j] = 1
                dfs(j+2,i,cnt+1)
                ladder[i][j] = 0
    


n,m,h = map(int,sys.stdin.readline().strip().split())
ladder = [[0] * n for _ in range(h)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().strip().split())
    ladder[a-1][b-1] = 1

ans = 4
dfs(0,0,0)

if ans == 4:
    print(-1)
else:
    print(ans)