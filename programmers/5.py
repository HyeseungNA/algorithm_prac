# begin == target
# words속 단어와 begin이 같을 때 해당 단어를 begin으로 바꿔줘/ count+=1


from collections import deque

def solution(begin, target, words):
    q = deque()
    used = deque()
    cnt = 0
    
    def check(char,begin):
        tmp_cnt = 0
        for i in range(len(begin)):
            #같은 글자면 count세주기
            if char[i] == begin[i]:
                tmp_cnt += 1
        if tmp_cnt == len(begin) -1 : # 같은 글자가 두개이면 True
            return True
        else:
            return False
    
    def bfs(char,target,words):
        nonlocal q,used
        

        # 단어가 바뀔때마다 cnt 더해주기
        while q:
            char,cnt = q.popleft()
            print(char)
            if char == target: # 현재 값이랑 target이랑 같으면
                return cnt # cnt를 return
            for string in words:
                #used배열에 없거나, check함수가 true이면
                if string not in used and check(string,char): 
                    used.append(string)
                    q.append([string,cnt+1]) # q에 넣어주기
        return 0
    
    if target not in words: # target이 words 리스트에 없다면
        return 0 # 0을 return 해주기
    
    # 시작점 찾기
    else: 
        for char in words:
            if check(char,begin): # 알파벳 하나만 다른지 체크하는 함수 호출
                cnt += 1
                q.append([char,cnt])
                used.append(char)

                result= bfs(char,target,words)
                # 결과값이 True이면 bfs를 
                if result:
                    return result
    return 0