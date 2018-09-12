from math import gcd

'''def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x'''

n = int(input())

for i in range(n):
    n1, barra1, d1, op, n2, barra2, d2 = input().split()
    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)

    if (op == '+'):
        num = (n1*d2 + n2*d1)
        dem = (d1*d2)
    elif (op == '-'):
        num = (n1*d2 - n2*d1)
        dem = (d1*d2)
    elif (op == '*'):
        num = (n1*n2)
        dem = (d1*d2)
    elif (op == '/'):
        num = (n1*d2)
        dem = (n2*d1)
    div = gcd(num, dem)
    numf = int(num / div)
    demf = int(dem / div)
    print('{}/{} = {}/{}'.format(num, dem, numf, demf))