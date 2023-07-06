def solution(brown,yellow):
    answer = []

    for i in range(1, yellow+1):

        if yellow % i == 0:
            yellow_col = i
            yellow_row = yellow // i

            if (yellow_1 + yellow_2) * 2 +4 == brown:
                return [yellow_row+2,yellow_col+2]
                
            