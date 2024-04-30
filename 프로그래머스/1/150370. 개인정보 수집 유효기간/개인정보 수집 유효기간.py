def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    ty,tm,td = map(int,today.split('.'))

    t_date = ty * 12 * 28 + tm * 28 + td
    
    
    for term in terms:
        name,date = term.split(' ')
        term_dic[name] = int(date)
        

    for i in range(len(privacies)):
        dateinfo, name = privacies[i].split(' ')
        
        year,month,date = map(int,dateinfo.split('.'))
        
        month += term_dic[name]
        year_diff = month // 12
        month = month  % 12
        year += year_diff
   
        p_date = year * 12 * 28 + month * 28 + date
        
        if t_date >= p_date:
            answer.append(i+1)
        
        
        
    return answer