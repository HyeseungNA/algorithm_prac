def solution(sequence, k):
    answer = []
    st = 0
    
    while st < len(sequence):
        total = 0
        for i in range(st,len(sequence)):
            total += sequence[i]
            if total == k:
                st += 1
                print(st,total)
                break
            
            elif total < k:
                continue
            else:
                st += 1
                break
        else:
            st += 1        
        
    return answer
solution([1, 2, 3, 4, 5],7)