def solution(sequence, k):
    answers = []
    total = 0
    l = 0
    r = 0
    total = sequence[l]
    while True:
        if total < k:
            r += 1
            if r >= len(sequence):
                break
            total += sequence[r]
        
        if total >= k:
            if total == k:
                answers.append([l,r])
            total -= sequence[l]
            l += 1
            if l >= len(sequence):
                break
        
    answers = sorted(answers, key=lambda x:(x[1]- x[0] , x[0]))
    return answers[0]