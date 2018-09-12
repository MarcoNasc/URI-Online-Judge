from math import floor

resi = {}
cidade = 0
while True:
    n = int(input('Nº de residências: '))
    if (n == 0):
        break
    else:
        cidade += 1
        for i in range(1, n+1):
            dados = []
            x, y = map(int, input("Nº de moradores e consumo total (m³): ").split())
            dados.append(x)
            dados.append(y)
            resi["resid{}".format(i)] = dados
            consumo = floor(resi["resid{}".format(i)][1]/resi["resid{}".format(i)][0])
            resi["resid{}".format(i)].append(consumo)
        ordemconsumo = sorted(resi.items(), key= lambda x: x[1][2])
        print('Cidade# {}'.format(cidade))
        quantgente = 0
        consumot = 0
        for casa in ordemconsumo:
            print('{}-{}'.format(casa[1][0], casa[1][2]), end=' ')
            quantgente += casa[1][0]
            consumot += casa[1][1]
        consumedio = consumot/quantgente
        print('\nConsumo medio: {:.2f} m3.'.format(consumedio))
        print()
        print(resi)
        print(ordemconsumo)
