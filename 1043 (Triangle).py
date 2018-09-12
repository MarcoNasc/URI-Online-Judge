a, b, c = map(float, input().split())
if ((a < (b + c)) and (b < (a + c)) and (c < (a + b))):
    peri = a + b + c
    print('Perimetro = {:.1f}'.format(peri))
else:
    area = ((a + b) * c)/2
    print('Area = {:.1f}'.format(area))
