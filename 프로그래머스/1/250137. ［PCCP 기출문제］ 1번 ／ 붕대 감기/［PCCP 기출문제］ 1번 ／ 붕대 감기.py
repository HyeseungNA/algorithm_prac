def solution(bandage, health, attacks):
    answer = 0
    time = 0
    now_health = health
    plus_time, sec_plus, plus = bandage[0],bandage[1],bandage[2] 
    for attack_time, attack_hurt in attacks:
        cnt = 0 # 연속성
        while time < attack_time:
            time += 1 # 시간 추가
            if time != attack_time: # 몬스터 공격 시간이 아니라면
                if now_health + sec_plus < health:
                    now_health += sec_plus # 1초마다 추가하는 회복량
                    cnt += 1 # 연속성 추가
                else:
                    now_health = health # 최대를 넘어가지 않게
            
                if cnt == plus_time: # 연속성 기준 충족되면
                    if now_health + plus <= health:
                        now_health += plus
                    else:
                        now_health = health
                    cnt = 0
        now_health -= attack_hurt
        if now_health <= 0:
            answer = -1
            break
        else:
            answer = now_health
                
            
            
    return answer