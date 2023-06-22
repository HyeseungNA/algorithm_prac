from collections import deque
# 외부 공기로 표시해주기

# 1이 사라질 때까지 반복

def find():


    q = deque()

    visited = [[0] * m for _ in range(n)]

    q.append((0,0))
    visited[0][0] = 1
    while q:
        
        y,x = q.popleft()
        # 외부공기 표시해주기
        ice[y][x] = 2
     

        dy = [-1,0,1,0]
        dx = [0,-1,0,1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 외부공기이고 방문을 안하면
            if 0<= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
                if ice[ny][nx] == 0 or ice[ny][nx] == 2:
                    visited[ny][nx] = 1
                    q.append((ny,nx))

# 얼음 녹이기
def melt(y,x):
    global ice_melt,melt_lst
    cnt = 0

    dy = [-1,0,1,0]
    dx = [0,-1,0,1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 외부공기를 만나면 개수 더해주기
        if 0 <= ny < n and 0 <= nx < m:
            if ice[ny][nx] == 2:
                cnt += 1
    
    # 외부공기가 2개 이상이면
    if cnt >= 2:
        # 외부 공기를 만들어주고
        # 얼음을 녹여줘
        melt_lst.append([y,x])


n,m = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(n)]

# 얼음 개수
ice_cnt = 0
result = 0
for i in range(n):
    ice_cnt += ice[i].count(1)
    

while ice_cnt > 0:

    # 다시 외부공기로 바꾸기
    find()

    # 녹일 얼음 리스트 초기화
    melt_lst = []

   
    
    # 얼음 녹이기
    for i in range(n):
        for j in range(m):
            if ice[i][j] == 1:
                melt(i,j)

    ice_melt = len(melt_lst)

    # 남은 얼음에서 녹은 얼음 빼주기
    ice_cnt -= ice_melt
    
    # 한꺼번에 얼음을 공기로 바꿔주기
    for y,x in melt_lst:
        ice[y][x] = 2

  
    
    result += 1

print(result)