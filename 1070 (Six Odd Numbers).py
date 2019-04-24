n = int(input())
if (n % 2 == 0):
    x = 0
else:
    x = 1
for i in range(n, n+12):
    if (i % 2 != 0):
        print(i)
        x =+1
        if (x == 6):
            break