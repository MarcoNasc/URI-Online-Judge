grenais = 0
inter = 0
gremio = 0
empate = 0

while True:
    grenais += 1
    i, g = map(int, input().split())
    if i > g:
        inter += 1
    elif i < g:
        gremio += 1
    else:
        empate += 1
    print('Novo grenal (1-sim 2-nao)')
    ng = int(input())
    if ng == 1:
        continue
    else:
        break

print('{} grenais'.format(grenais))
print('Inter:{}'.format(inter))
print('Gremio:{}'.format(gremio))
print('Empates:{}'.format(empate))

if inter > gremio:
    print('Inter venceu mais')
elif gremio > inter:
    print('Gremio venceu mais')
else:
    print('Não houve vencedor')
