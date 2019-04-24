n = int(input())
ins = out = 0
for i in range(n):
    m = int(input())
    if (m in range(10, 21)):
        ins += 1
    else:
        out += 1
print('{} in'.format(ins))
print('{} out'.format(out))
