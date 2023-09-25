tri = [int(input()) for _ in range(3)]


if sum(tri) != 180:
    print('Error')

else:
    if len(set(tri)) == 2:
        print('Isosceles')
    
    if len(set(tri)) == 3:
        print('Scalene')
    if len(set(tri)) == 1:
        print('Equilateral')