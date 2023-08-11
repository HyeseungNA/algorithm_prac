from fractions import gcd

def solution(arr):

    answer = arr[0]

    for num in arr:
        answer = (num * answer) // gcd(answer,num)
    return answer