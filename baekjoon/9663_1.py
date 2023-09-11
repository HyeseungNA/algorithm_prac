# 세로 확인
# 좌상향 대각선
# 우상향 대각선

def dfs(cnt):
    global total
    # 깊이가 n과 같으면 return
    if cnt == n:
        total += 1
        return
    
    for i in range(n):
        # 세로 방문 안하고, 대각선 방문 안하면,,,
        if v1[i] == 0 and v2[i - cnt] == 0 and v3[(cnt + i)] == 0:
            # 방문 처리해주고
            v1[i] = 1
            v2[i - cnt] = 1
            v3[cnt + i] = 1
            # 다음으로 이동이요~
            dfs(cnt+1)
            # 다시 원상복구 해주쇼
            v1[i] = 0
            v2[i - cnt] = 0
            v3[cnt + i] = 0
    

n = int(input())
# 세로 확인
v1 = [0] *  n
# 좌상향 대각선 확인
v2 = [0] * 2 * n
# 우상향 대각선 확인
v3 = [0] * 2 * n
total = 0
dfs(0) # cnt
# 다 만족하면 이동하기

print(total)