a, b = map(int, input().split())
if (a < b):
    tempo = b - a
else:
    tempo = 24 - a + b
print('O JOGO DUROU {} HORA(S)'.format(tempo))
