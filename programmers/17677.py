from collections import Counter
import math
def solution(str1, str2):
    # 예외처리
    # 교집합은 for문으로
    # 합집합은 그냥 extend로
    
    answer = 0
    
    str1 = str1.lower()  # str1을 모두 소문자로 변환
    str2 = str2.lower()  # str2를 모두 소문자로 변환
    
    # print(str1,str2)
    
    # 인덱싱 해서 넣어주는 리스트
    a = []
    b = []
    
    # 교집합 리스트
    intersect = []
    
    # 합집합 리스트
    union = []
    

    
    # 인덱싱으로 끊어주기
    for i in range(len(str1)- 1):
        flag = 0
        for j in range(2):
            if ord(str1[j+i]) >= 65 and ord(str1[j+i]) <= 90 or (ord(str1[j+i]) >= 97 and ord(str1[j+i]) <= 122):
                continue
            else:
                flag = 1
        if flag == 0:
            a.append(str1[i:i+2])
    
    
    # 인덱싱으로 끊어주기
    for i in range(len(str2)- 1):
        flag = 0
        for j in range(2):
            if ord(str2[j+i]) >= 65 and ord(str2[j+i]) <= 90 or (ord(str2[j+i]) >= 97 and ord(str2[j+i]) <= 122):
                continue
            else:
                flag = 1
        if flag == 0:
            b.append(str2[i:i+2])
    
    Counter_a = Counter(a)
    Counter_b = Counter(b)

    inter = list((Counter_a & Counter_b).elements())
    union = list((Counter_a | Counter_b).elements())
    
   

    if len(inter) == 0 and len(union) == 0: # 공집합일 때 
        answer = 65536

    else:
        answer = (len(inter) / len(union)) * 65536
    
    
    
    
    
    return math.floor(answer)