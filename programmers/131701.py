def solution(elments):
    answer = 0
    elmentsLen = len(elments)
    elments = elments * 2
    numberSet = set()

    for i in range(elmentsLen):
        for j in range(elmentsLen):
            numberSet.add(elements[j:i + j + 1])
    
    return len(numberSet)
