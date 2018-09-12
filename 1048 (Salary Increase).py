sal = float(input())
if (0 < sal <= 400):
    percent =  0.15
elif (400 < sal <= 800):
    percent = 0.12
elif (800 < sal <= 1200):
    percent = 0.10
elif (1200 < sal <= 2000):
    percent = 0.07
else:
    percent = 0.04
novosal = sal + (sal*percent)
reajuste = novosal - sal
print('Novo salario: {:.2f}'.format(novosal))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(int(percent*100)))
