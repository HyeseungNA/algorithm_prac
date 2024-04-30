def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower() 
    # 2단계
    com = ['-','_','.']
    for id in new_id:
        if not id.isdigit():
            if not id.isalpha() and id not in com:
                new_id = new_id.replace(id,'')
    
    # 3단계
    cnt = 0
    tmp = ''
    # for id in new_id:
    #     if id == '.':
    #         cnt += 1
    #         tmp += id
    #     else:
    #         if cnt >= 2:
    #             new_id = new_id.replace(tmp,'.')
    #             tmp = ''
    #             cnt = 0
    
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    print(new_id)
    
    # 4단계
    if len(new_id) >= 1 and new_id[0] == '.':
        new_id = new_id[1:]
     
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 5단계
    if len(new_id) == 0:
        new_id += 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
    
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    
    answer = new_id
    return answer