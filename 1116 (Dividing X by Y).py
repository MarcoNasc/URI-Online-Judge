n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    try:
        print('{:.1f}'.format(x/y))
    except ZeroDivisionError:
        print('divisao impossivel')
