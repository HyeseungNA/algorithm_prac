def solution(citations):
    citations.sort()
    n = 0
    while True:
        st = 0
        ed = 0
        for num in citations:
            if n <= num:
                st += 1
            else:
                ed += 1
        if st < ed:
            break
        n += 1

    return n - 1

result = solution([3, 0, 6, 1, 5])
