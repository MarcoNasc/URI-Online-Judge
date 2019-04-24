while True:
    a, b = map(int, input().split())
    if a == b:
        break
    else:
        if a < b:
            print('Crescente')
        else:
            print('Decrescente')
            