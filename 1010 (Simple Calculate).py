list1 = input().split()
list2 = input().split()

total = int(list1[1])*float(list1[2]) + int(list2[1])*float(list2[2])
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
