while True:
    n1 = float(input())
    if (0 > n1 or n1 > 10 ):
        print('nota invalida')
    else:
        while True:
            n2 = float(input())
            if (0 > n2 or n2 > 10 ):
                print('nota invalida')
            else:
                print('media = {}'.format((n1+n2)/2))
                print('novo calculo (1-sim 2-nao)')
                while True:
                    r = int(input())
                    if (r == 1):
                        continue
                    elif (r == 2):
                        break
                    else:
                        continue