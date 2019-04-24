'''t = int(input())
for x in range(n):'''
n, k = map(int, input().split())
l1 = []
l2 = []
for i in range(1, n+1):
    l1.append(i)
while (len(l1) > 1):
    ind = 0
    l2.append(l1[ind+k])
    del l1[ind+k]
print(l2)
print(l1)
