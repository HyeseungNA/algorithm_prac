from collections import Counter

def solution(want, number, discount):
    # 상품들과 수량을 딕셔너리에 넣기
    # 할인 날짜들을 돌면서 딕셔너리 value값과 비교하기
    answer = 0
    # for i in range(len(discount) -9 ):
    #     products = []
    #     for good,num in zip(want,number):
    #         products.extend([good] * num)
        
    #     compare = discount[i:i+10]

    #     products.sort()
    #     compare.sort()

    #     if products == compare:
    #         answer += 1
    # # print(answer)
    # return answer
        
    products = dict(zip(want,number))
    for i in range(len(discount) - 9):
        if products == Counter(discount[i:i+10]):
            answer += 1
    return answer
solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])