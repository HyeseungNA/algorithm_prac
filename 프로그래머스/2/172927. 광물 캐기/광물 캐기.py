def solution(picks, minerals):
    # minerals 리스트를 5개씩 묶어 2차원 리스트로 반환
    # 곡괭이를 모두 사용했는데 광물이 남아 있는 경우는 min 함수를 통해 제외
    minerals = [list(minerals[i:i+5]) for i in range(0, min(sum(picks)*5, len(minerals)), 5)]
    req = []
    
    # 각 묶음에서 곡괭이별로 필요한 피로도를 계산하여 반환
    for bundle in minerals:
        tmp = [0,0,0]
        
        for i in bundle:
            tmp[0] += 1
            tmp[1] += 5 if i == "diamond" else 1
            tmp[2] += 25 if i == "diamond" else 5 if i == "iron" else 1
            
        req.append(tmp)
    
    # 낮은 등급의 곡괭이 점수를 기준으로 내림차순 정렬
    req.sort(key=lambda x:(-x[2],-x[1]))
    
    # 다이아몬드 곡괭이부터 순서대로 사용
    ans = 0
    for score in req:
        if picks[0]:
            ans += score[0]
            picks[0] -= 1
        elif picks[1]:
            ans += score[1]
            picks[1] -=1
        elif picks[2]:
            ans += score[2]
            picks[2] -= 1
        else:
            break
    
    return ans