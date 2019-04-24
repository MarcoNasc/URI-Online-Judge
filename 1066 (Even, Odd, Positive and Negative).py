par = impar = pos = neg = 0
for i in range(5):
    j = int(input())
    if (j % 2 == 0):
        par += 1
    else:
        impar += 1
    if (j > 0):
        pos += 1
    elif (j < 0):
        neg += 1
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))
