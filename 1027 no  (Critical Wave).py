while True:
    n = int(input())
    pontos = 0
    lastx = lasty = 0
    for i in range(n):
        x, y = map(int, input().split())
        if (i == 0):
            lastx = x
            lasty = y
            pontos += 1
        if(abs(y - lasty) == 2):
            lastx = x
            lasty = y
            pontos += 1
            a = abs(y - lasty)/2
