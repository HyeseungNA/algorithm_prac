from collections import defaultdict
s,e,q = input().split()
st = int(s.split(':')[0]) * 60 + int(s.split(':')[1])
ed = int(e.split(':')[0]) * 60 + int(e.split(':')[1])
ed_s = int(q.split(':')[0]) * 60 + int(q.split(':')[1])
enter = defaultdict(int)
out = defaultdict(int)
while True:
    try:
        hour, name = input().split()
        hour = int(hour.split(':')[0]) * 60 + int(hour.split(':')[1])
        if hour <= st:
            enter[name] += 1
        elif ed <= hour <= ed_s:
            out[name] += 1

    except:
        break
cnt = 0
for key in enter.keys():
    if key in out:
        cnt += 1
    

print(cnt)