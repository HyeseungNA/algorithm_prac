import sys
sys.setrecursionlimit(10 ** 6)

T = int(input())
for _ in range(T):
    def dfs(level,idx):
        global answer
        # 다 채워지면 개수 더해주기
        if level == n:
            answer += 1
            return
        
        for i in range(idx,m):
            if visited[i] == 0:
                visited[i] = 1
                # 다리에 연결할 지점 넣어주기
                bridge[level] = point[i]
                # 겹치면 안되니까 현재 지점 이상부터
                dfs(level+1,i+1)
                visited[i] = 0


    n,m = map(int,input().split())
    bridge = [0] * n
    visited = [0] * m
    point = [0] * m
    answer = 0
    # 처음 시작
    dfs(0,0)
    print(answer)


