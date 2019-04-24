#dado n, qual o menor número com n divisores? Ex. n = 4, reposta = 6 (1, 2, 3 e 6).
import time
from math import *
start_time = time.time()


def n_divisors(num):
    cont = 1
    #div = []
    for k in range(1, round(num/2)+1):
        if num % k == 0:
            cont += 1
            #div.append(k)
    return cont #, div)


def num_n_div(n):
    num = (n-1)
    while True:
        num += 1
        if n_divisors(num) == n:
            break
    return num

print(n_divisors(10))

'''
m = int(input())
for i in range(m):
    n = int(input())
    print(num_n_div(n))
'''

print("--- %s seconds ---" % (time.time() - start_time))