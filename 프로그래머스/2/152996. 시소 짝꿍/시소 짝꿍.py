from collections import defaultdict

def solution(weights):
    answer = 0

    weights_dict = defaultdict(int)
    ratio = [1/1, 1/2, 2/1, 2/3, 3/2, 3/4, 4/3]
    
    for weight in weights:
        for r in ratio:
            answer += weights_dict[weight * r]
        
        weights_dict[weight] += 1
    
    return answer