
def solution(n):
    answer = ''

    
    lst = [4,1,2]
    while n:
        n,na = divmod(n,3)
        answer = str(lst[na]) + answer
        if na == 0:
            n -= 1
        
    return answer