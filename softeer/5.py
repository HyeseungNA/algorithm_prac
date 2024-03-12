import sys
word = input()
key = input()
alphabet = ['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
map = [[''] * 5 for _ in range(5)]


k = 0
  for i in range(5):
    for j in range(5):
        while k < len(key):
            if key[k] in alphabet:
                map[i][j] = key[k]
                alphabet.remove(key[k])
                
            k += 1
        
print(map)

'''
HELLOWORLD
HELLOWORLD
'''