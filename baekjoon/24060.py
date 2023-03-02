def mergeSort(L):
    print(L)
    if len(L) == 1:
        return L
    
    mid = (len(L) + 1)//2
    left = mergeSort(L[:mid])
    print('---',left)
    print(L[mid:])
    right = mergeSort(L[mid:])
    print(right)
 

n= [1,4,6,5,7,8,9,2]
mergeSort(n)