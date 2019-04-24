from math import sqrt, pow

while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())
        dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        if r1 >= (dist + r2):
            print('RICO')
        else:
            print('MORTO')
    except EOFError:
        break
