n = int(input())
for i in range(n):
    j = int(input())
    if (j % 2 == 0 and j!= 0):
        print('EVEN ', end='')
    elif(j % 2 != 0 and j != 0):
        print('ODD ', end='')
    if (j > 0):
        print('POSITIVE')
    elif (j < 0):
        print('NEGATIVE')
    else:
        print('NULL')
