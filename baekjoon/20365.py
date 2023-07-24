n = int(input())

colors = list(input())

color = {'R': 0, 'B':0}

color[colors[0]] += 1

for i in range(1,n):
    if colors[i] != colors[i-1]:
        color[colors[i]] += 1

print(min(color['R'], color['B']) + 1)