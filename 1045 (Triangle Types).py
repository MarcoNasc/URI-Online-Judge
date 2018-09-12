a, b, c = map(float, input().split())
if ((a < (b + c)) and (b < (a + c)) and (c < (a + b))):
    if (a**2 == b**2 + c**2):
        print('TRIANGULO RETANGULO')
    if (a**2 > b**2 + c**2):
        print('TRIANGULO OBTUSANGULO')
    if (a**2 < b**2 + c**2):
        print('TRIANGULO ACUTANGULO')
    if (a == b == c):
        print('TRIANGULO EQUILATERO')
    elif ((a == b) or (a == c) or (b == c)):
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
