def fibo(n, d):
    if n in d:
        return d[n]
    else:
        ans = fibo(n-1, d) + fibo(n-2, d)
        d[n] = ans
        return ans

d = {1: 0, 2: 1}

n = int(input())

for i in range(1, n+1):
    if i != n:
        print(fibo(i, d), end=' ')
    else:
        print(fibo(i, d))
        