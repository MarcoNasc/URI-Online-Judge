valor = int(input(''))
anos = meses = dias = 0
while (valor >= 365):
    valor -= 365
    anos += 1
while (valor >= 30):
    valor -= 30
    meses += 1
while (valor >= 1):
    valor -= 1
    dias += 1
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias)
      