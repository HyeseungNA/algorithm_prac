def solution(elments):

    elmentsLen = len(elments)
    elements = elements * 2
    result = set()

    for i in range(elmentsLen):
        for j in range(elmentsLen):
            result.add(sum(elements[j:i+j]))


    
    return len(result)
