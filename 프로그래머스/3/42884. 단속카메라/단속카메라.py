def solution(routes):
    answer = 0
    routes.sort(key=lambda x:(x[1],x[0]))
    
    camera = -30001
    
    for i,o in routes:
        if i <= camera:
            continue
        else:
            answer += 1
            camera = o
    
    return answer