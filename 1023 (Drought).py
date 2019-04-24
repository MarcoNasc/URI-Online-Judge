from math import floor

resi = {}
cidade = 0
while True:
    n = int(input('Nº de residências: '))
    #condição de parada
    if (n == 0):
        break
    else:
        #conta a cidade porque tem que imprimir depois
        cidade += 1
        #loop pra pegar as info de cada casa
        for i in range(1, n+1):
            dados = []
            x, y = map(int, input("Nº de moradores e consumo total (m³): ").split())
            dados.append(x)
            dados.append(y)
            #casa redidência é uma chave dentro do dicionário
            #o valor de cada chave é uma lista com as três informações
            resi["resid{}".format(i)] = dados
            #consumo médio da casa arredondado pra baixo é o terceiro elemento da lista
            consumo = floor(resi["resid{}".format(i)][1]/resi["resid{}".format(i)][0])
            resi["resid{}".format(i)].append(consumo)
        #ordeno o dicionário de acordo com consumo médio usando a função lambda
        ordemconsumo = sorted(resi.items(), key= lambda x: x[1][2])
        print('Cidade# {}'.format(cidade))
        #agora calcular o consumo médio total
        quantgente = 0
        consumot = 0
        #imprime número de pessoas e consumo médio por casa
        for casa in ordemconsumo:
            print('{}-{}'.format(casa[1][0], casa[1][2]), end=' ')
            quantgente += casa[1][0]
            consumot += casa[1][1]
        #consumo médio total que é com os valores sema arredondamento
        consumedio = consumot/quantgente
        print('\nConsumo medio: {:.2f} m3.'.format(consumedio))
        print()
        #imprimindo só pra ver como tá
        print(resi)
        print(ordemconsumo)
        #depois faz o loop pra próxima cidade até o input ser 0
