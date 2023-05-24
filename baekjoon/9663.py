# 깊이가 n이랑 같으면 return 
# 다음 노드가 세로, 가로, 대각선에 위치하면 안돼

def dfs(y,x):

    found(y,x)
    global cnt
    # 깊이가 n이면 return 
    if depth == n:
        # 경우의 수 더해줘야해
        cnt+=1
        return
    # queens에 queen 넣어줘

    # 다음 queen 찾아
    found(y,x)



# 다음 queen 찾는 함수
def found(y,x):
    for i in range(n):
    # 범위 확인
        if 0 <= i < n and

    # 가로 확인
        i !=n

    # 세로 확인
    

    # 대각선 확인

    # 다음 퀸 이어서 dfs
    




n= int(input())
queens = [[0] * n for _ in range(n)]

depth = 0
cnt = 0

queens[0][0]

dfs(0,0)

print(cnt)