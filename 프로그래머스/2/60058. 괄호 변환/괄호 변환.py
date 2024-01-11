def is_check(u):
    tmp = []
    u = list(u)
    
    i = 0
    while u:
        now = u.pop(0)
        if not tmp:
            tmp.append(now)
        else:
            if tmp[-1] == '(' and now == ')':
                tmp.pop()
            else:
                tmp.append(now)
        
    if tmp:
        return False
    else:
        return True

def is_balance(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        elif p[i] == ')':
            right += 1
        
        if right == left:
            return p[:i+1] , p[i+1:]
        
def solution(p):
    answer = ''
    if p == '':
        return ''
    
    u,v = is_balance(p)
    
    if is_check(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in range(1,len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
        
        return answer