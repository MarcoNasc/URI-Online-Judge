from decimal import Decimal
i = 0

while i <= 2:
    j = 1
    for m in range(3):
        if i == 1 or i == 2:
            i = int(i)
            print('I={} J={}'.format(i, j + i))
            j += 1
        else:
            print('I={} J={}'.format(i, j + i))
            j += 1
    i += Decimal('0.2')
