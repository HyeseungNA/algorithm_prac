def solution(players, callings):
    answer = []
    player = {name : i for i,name in enumerate(players)}
    score_sort = {i : name for i,name in enumerate(players)}

    for calling in callings:
        now_idx = player[calling]
        front_idx = now_idx - 1
        
        front_name = score_sort[front_idx] # 앞에 사람
        score_sort[front_idx] = calling # 앞으로 이동
        score_sort[now_idx] = front_name #  앞에 사람을 뒤로 
        player[front_name] = now_idx
        player[calling] = front_idx
    
    answer = list(score_sort.values())
        
    return answer