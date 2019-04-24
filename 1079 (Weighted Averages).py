n = int(input())
for i in range(n):
    n1, n2, n3 = map(float, input().split())
    media = (2*n1 + 3*n2 + 5*n3)/10
    print('{:.1f}'.format(media))
