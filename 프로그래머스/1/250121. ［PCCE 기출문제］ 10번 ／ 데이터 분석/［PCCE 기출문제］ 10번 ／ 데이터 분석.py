def solution(data, ext, val_ext, sort_by):
    answer = []
    idx1 = 0
    idx2 = 0
    ext_dic = {'code':0,'date':1,'maximum':2,'remain':3}
    sort_dic = {'code':0,'date':1,'maximum':2,'remain':3}
    
    idx1 = ext_dic[ext]
    idx2 = sort_dic[sort_by]
    
    for d in data:
        if d[idx1] <= val_ext:
            answer.append(d)
            
    answer.sort(key=lambda x:x[idx2])
    
    return answer