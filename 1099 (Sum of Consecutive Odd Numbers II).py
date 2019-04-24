n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    sum = 0
    if (a > b):
        A = b
        B = a
        for i in range(A + 1, B):
            if (i % 2 != 0):
                sum += i
    elif (b > a):
        A = a
        B = b
        for i in range(A + 1, B):
            if (i % 2 != 0):
                sum += i
    print(sum)
