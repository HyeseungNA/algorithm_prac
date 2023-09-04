# 세로 시작
# 가로 인접 확인 & 대각선 확인

def dfs(y,x):
    if y == n:
        cnt += 1
        return

    for i in range(n):
        # 가로 확인 및 대각선 확인
        if v1[i] == 0:
            # 대각선 확인에서 틀림
            if abs((y+1)-y) != abs(i-x):
                v1[i] = 1
                v2[y+1][i] = 1
                dfs(y+1,)

        
        return

n = int(input())
v1 = [0] * n
v2 = [[0] * n for _ in range(n)]
cnt = 0
for i in range(n):
    # 방문처리해주기
    v2[0][i] = 1
    # 가로 방문 처리
    v1[i] = 1
    dfs(0,i) # 세로 시작, 가로 인덱스
    v2[0][i] = 0
    v1[i] = 0
