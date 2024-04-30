def solution(park, routes):
    answer = []
    n = len(park)
    m = len(park[0])
    parks = []
    orders = {'E': [0,1], 'S': [1,0], 'N': [-1,0], 'W': [0,-1]}
    for p in park:
        parks.append(list(p))
    

    for i in range(n):
        for j in range(m):
            if parks[i][j] == 'S':
                y,x = i,j
                break
    
    
    for route in routes:
        dir,distance = route.split(' ')
        distance = int(distance)
        
        st_y,st_x = y,x # 원래 위치

        for _ in range(distance):
            ny,nx = y + orders[dir][0], x + orders[dir][1]
            if 0 <= ny < n and 0 <= nx < m and parks[ny][nx] != 'X':
                y,x = ny,nx
            
            else:
                y,x = st_y,st_x
                break
            
        answer = [y,x]
            
      
    
    return answer