def solution(clothes):
    answer = 1
    dic = dict()
    # 딕셔너리에 넣고
    # 딕셔너리에 넣기
    for c in clothes:
        if c[1] not in dic:
            dic[c[1]] = 1
        else:
            dic[c[1]] += 1
    
    for value in dic.values():
        answer *= (value + 1)
    
    return answer - 1
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])