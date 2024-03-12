# import copy
# from itertools import permutations


# def solution(expression):
#     compute = ['-','*','+']
#     computes_lst = list(permutations(compute,3)) # 연산자로 만들수 있는 경우의수
#     tmp = ''
#     lst = []
#     answer = int(-21e8)
#     # 연산 기호 & 숫자 따로 저장
#     for ex in expression:
#         if ex not in compute:
#             tmp += ex
#         else:
#             lst.append(int(tmp))
#             lst.append(ex)
#             tmp = ''
    
#     lst.append(int(tmp))
    
#     for computes in computes_lst:
#         lst2 = copy.deepcopy(lst)
#         for com in computes:
#             while True:
#                 if com not in lst2:
#                     break
#                 for i in range(len(lst2)):
#                     if com == lst2[i] and com == '*':
#                         change = lst2[i-1] * lst2[i+1]
#                         del lst2[i-1:i+2]
#                         lst2.insert(i-1,change)
#                         break
#                     if com == lst2[i] and com == '+':
#                         change = lst2[i-1] + lst2[i+1]
#                         del lst2[i-1:i+2]
#                         lst2.insert(i-1,change)
#                         break
#                     if com == lst2[i] and com == '-':
#                         change = lst2[i-1] - lst2[i+1]
#                         del lst2[i-1:i+2]
#                         lst2.insert(i-1,change)
#                         break
#         answer = max(answer,abs(*lst))

#     return answer
# solution("100-200*300-500+20")

word = "abcabb"
print(word.replace('b','')) # b를 공백으로 바꾸겠다. 
print(word) # word = "aca"