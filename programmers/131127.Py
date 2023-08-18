from collections import Counter

def solution(want, number, discount):
    answer = 0
    products = []
    for p,n in zip(want,number):
        products.extend([p] * n)
    products.sort()

    for i in range(len(discount) - 9):
        com = discount[i:i+ 10]
        com.sort()
        if com == products:
            answer += 1

    return answer

    
    
solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])