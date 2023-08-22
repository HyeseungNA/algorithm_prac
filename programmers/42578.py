def solution(clothes):
    # 아이템을 넣을 딕셔너리
    item = {}
    answer = 1
    for c in clothes:
        if c[1] in item:
            item[c[1]] += 1
        else:
            item[c[1]] = 1
    for value in item.values():
        answer *= (value  + 1)
    print(answer)
    return answer - 1
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])