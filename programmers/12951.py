def solution(s):
    s = s.split(" ")
    answer = []
    for word in s:
        
        if word:
            answer.append(word.capitalize())
        
        else:
            answer.append(word)
    return " ".join(answer)
        
