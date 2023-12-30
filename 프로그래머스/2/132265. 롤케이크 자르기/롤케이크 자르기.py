from collections import Counter
def solution(topping):
    idx = 0
    answer = 0
    chulsu = Counter(topping)
    bro = {}
    for t in topping:
        chulsu[t] -= 1
        if t not in bro:
            bro[t] = 1
        else:
            bro[t] += 1
        
        if chulsu[t] == 0:
            chulsu.pop(t)
        # print(chulsu, bro)
        if len(bro) == len(chulsu):
            answer += 1
    return answer


