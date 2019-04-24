a = g = d = 0
print('MUITO OBRIGADO')

while True:
    t = int(input())
    if t == 4:
        break
    elif t not in range(1, 5):
        continue
    else:
        if t == 1:
            a += 1
        elif t == 2:
            g += 1
        elif t == 3:
            d += 1

print('Alcool: {}'.format(a))
print('Gasolina: {}'.format(g))
print('Diesel: {}'.format(d))
