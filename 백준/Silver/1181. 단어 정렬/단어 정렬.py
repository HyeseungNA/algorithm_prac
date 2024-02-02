n = int(input())
lst = []
for _ in range(n):
    word = input()
    if word not in lst:
        lst.append(word)

sorted_lst = sorted(lst,key=lambda x:(len(x),x))
for el in sorted_lst:
    print(el)
    
