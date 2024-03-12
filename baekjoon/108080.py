# alpabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [0] * 26
word = input()


for w in word:
    numbers[ord(w.upper())- 65] += 1
print(*numbers)