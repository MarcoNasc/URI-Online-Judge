A, B, C = map(float, input().split())

areatri = (A*C)/2
pi = 3.14159
areacir = pi*(C**2)
areatrap = ((A + B) * C)/2
areasqr = B*B
arearect = A*B

print('TRIANGULO: {:.3f}'.format(areatri))
print('CIRCULO: {:.3f}'.format(areacir))
print('TRAPEZIO: {:.3f}'.format(areatrap))
print('QUADRADO: {:.3f}'.format(areasqr))
print('RETANGULO: {:.3f}'.format(arearect))