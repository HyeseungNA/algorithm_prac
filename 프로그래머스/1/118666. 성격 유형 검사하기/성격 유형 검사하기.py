def solution(survey, choices):
    answer = ''
    p = {'R':0, 'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for i in range(len(survey)):
        if choices[i] <= 3:
            p[survey[i][0]] += 4 - choices[i]
        
        else:
            p[survey[i][1]] += choices[i] - 4 
            
    if p['R'] >= p['T']:
        answer += 'R'
    if p['R'] < p['T']:
        answer += 'T'
    
    if p['C'] >= p['F']:
        answer += 'C'
    if p['C'] < p['F']:
        answer += 'F'

    if p['J'] >= p['M']:
        answer += 'J'
    if p['J'] < p['M']:
        answer += 'M'
    
    if p['A'] >= p['N']:
        answer += 'A'
    
    if p['A'] < p['N']: 
        answer += 'N'
     
    
        
    
    return answer