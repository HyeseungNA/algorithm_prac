from collections import deque
def bfs(y,x,map):
    global q
        
    # q가 있을 동안 계속 이동해랏
    while q:
        
        y,x,cnt = q.popleft()
        # 적의 위치면 cnt 를 return 해줘라!
    
        if y ==  len(map)- 1 and x == len(map[0]) -1:
            return cnt
              
    
        
        dy = [-1,0,1,0]
        dx = [0,-1,0,1]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # 범위 안에 있고 이동할 수 있으면
            if 0 <= ny < len(map) and 0 <= nx < len(map[0]) and map[ny][nx] == 1:
                map[ny][nx] = 0 #map을 바꿔주고
                q.append([ny,nx,cnt+1]) # q에 넣어줘
    
    # 현재 값이 적의 위치에 존재하지 않으면 -1로 만들어버리기
    return -1
    
def solution(map):
    global q
    q = deque()
    answer = 0
    answer_list = []
    
    # 시작점을 찾아서 bfs 시작하기
    q.append([0,0,1])
    map[0][0] = 0
    cnt = bfs(0,0,map)
    return cnt
    
