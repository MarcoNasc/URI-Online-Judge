x, y = map(int, input().split())

c = 0

while c < y:
    for i in range(x):
        if c >= y:
            break
        else:
            c += 1
            if i == x-1:
                print(c, end='\n')
            else:
                print(c, end=' ')
