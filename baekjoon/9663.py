# 세로 시작
# 가로 인접 확인 & 대각선 확인

def dfs(y):
    global cnt
    if y == n:
        cnt += 1
        return

    for i in range(n):
        # 가로 확인, 우상향 확인, 좌상향 확인
        if v1[i] == 0 and v2[y + i] == 0 and v3[y - i] == 0:
            v1[i] = v2[y+i] = v3[y - i] = 1
            dfs(y+1)
            v1[i] = v2[y+i] = v3[y - i] = 0
        

n = int(input())
# 가로확인
v1 = [0] * (2 * n)
# 우상향 확인
v2 = [0] * (2 * n)
# 좌상향 확인
v3 = [0] * (2 * n)

# 총 개수
cnt = 0
dfs(0)
print(cnt)