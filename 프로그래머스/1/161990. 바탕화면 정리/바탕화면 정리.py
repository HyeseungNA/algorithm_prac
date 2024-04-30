def solution(wallpaper):
    paper = []
    for wall in wallpaper:
        print(wall)
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                paper.append([i,j])
    
    Min_x = int(12e8)
    Min_y = int(12e8)

    for p in paper:
        Min_y = min(Min_y,p[0])
        Min_x = min(Min_x,p[1])
    
    
        
    Max_x = int(-12e8)
    Max_y = int(-12e8)
    
    for p in paper:
        Max_y = max(Max_y,p[0]+1)
        Max_x = max(Max_x,p[1]+1)
    
    answer = [Min_y,Min_x,Max_y,Max_x]
    return answer