from math import floor

n = int(input())
for i in range(n):
    pa, pb, ga, gb = map(float, input().split())
    anos = 0
    while True:
        pa += floor(pa*(ga/100))
        pb += floor(pb*(gb/100))
        anos += 1
        if (anos > 100):
            print('Mais de 1 seculo.')
            break
        elif (pa > pb):
            print('{} anos.'.format(anos))
            break
