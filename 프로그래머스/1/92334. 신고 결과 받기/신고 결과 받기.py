

def solution(id_list, report, k):
    answer = []
    calling_cnt = {id :0 for id in id_list}
    person = {id: set() for id in id_list}

    
    for re in report:
        do,done = re.split(' ')
        person[done].add(do)
    

    for key, values in person.items():
        if len(values) >= k:
            for v in values:
                calling_cnt[v] += 1
    
    answer = list(calling_cnt.values())
                
    
    
    return answer