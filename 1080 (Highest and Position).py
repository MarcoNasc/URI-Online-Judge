L = []
for i in range(1, 101):
    n = int(input())
    L.append(n)
print(max(L))
print(L.index(max(L)) + 1)
