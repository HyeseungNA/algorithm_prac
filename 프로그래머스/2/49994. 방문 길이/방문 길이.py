def solution(dirs):
    command = {'U': (0,1), 'D' : (0, -1) , 'L': (-1, 0) , 'R': (1,0)}
    road = set()
    y,x = (0,0)
    
    for d in  dirs:
        ny = y + command[d][1]
        nx = x + command[d][0]
        
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            road.add((ny,nx,y,x))
            road.add((y,x,ny,nx))
            y = ny
            x = nx
    answer = len(road) // 2
    return answer