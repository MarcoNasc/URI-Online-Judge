n = int(input())

c = r = s = 0
for i in range(n):
    num, ani = input().split()
    num = int(num)
    if ani == 'C':
        c += num
    elif ani == 'R':
        r += num
    elif ani == 'S':
        s += num

total = c + r + s
print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))

cpc = (c/total)*100
rpc = (r/total)*100
spc = (s/total)*100

print('Percentual de coelhos: {:.2f} %'.format(cpc))
print('Percentual de ratos: {:.2f} %'.format(rpc))
print('Percentual de sapos: {:.2f} %'.format(spc))

