sal = float(input())
totaltax = 0

if 0 < sal <= 2000:
    print('Isento')
elif 2000 < sal <= 3000:
    sal -= 2000
    tax = 0.08
    totaltax += tax*sal
    print('R$ {:.2f}'.format(totaltax))
elif 3000 < sal <= 4500:
    sal -= 2000
    tax1 = 0.08
    totaltax += tax1*1000
    sal -= 1000
    tax2 = 0.18
    totaltax += sal*tax2
    print('R$ {:.2f}'.format(totaltax))
elif 4500 < sal:
    sal -= 2000
    tax1 = 0.08
    totaltax += tax1 * 1000
    sal -= 1000
    tax2 = 0.18
    totaltax += tax2 * 1500
    sal -= 1500
    tax3 = 0.28
    totaltax += sal * tax3
    print('R$ {:.2f}'.format(totaltax))

