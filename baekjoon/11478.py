from collections import defaultdict
word = input()
n = len(word)
dic = defaultdict(int)

length = 1

while length <= n:
    for i in range(n-length+1):
        now =word[i:i+length]
        if dic[now]:
            continue
        else:
            dic[now] = 1

    length += 1
print(len(dic))