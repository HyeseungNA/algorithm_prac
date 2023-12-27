from itertools import product
def solution(word):
    answer = 0
    dic = ['A','E','I','O','U']
    i = 1
    lst = []
    while (i <= 5):
        lst += list(product(dic,repeat = i))
        
        i += 1
    lst.sort()
    for j in range(len(lst)):
        if lst[j] == tuple(word):
            answer = j + 1
            break
     
    return answer