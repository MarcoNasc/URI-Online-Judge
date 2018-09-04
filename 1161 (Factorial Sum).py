from math import factorial as fct

while True:
    try:
        L = input().split()

        M = int(L[0])
        Mfct = fct(M)

        N = int(L[1])
        Nfct = fct(N)

        print(Nfct + Mfct)
    except (EOFError):
        break
