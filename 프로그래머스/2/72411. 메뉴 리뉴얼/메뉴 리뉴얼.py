from itertools import combinations
def solution(orders, course):
    answer = []
    
    for i in course:
        alphabet = {}
        for order in orders:
            order = list(combinations(order,i))

            for o in order:
                o = list(o)
                o.sort()
                o = ''.join(o)
                if o not in alphabet:
                    alphabet[o] = 1
                else:
                    alphabet[o] += 1
        
        
     
        for key, value in alphabet.items():
            if value > 1 and value == max(alphabet.values()):
                answer.append(key)
        
        i += 1
    answer.sort()
    
    return answer