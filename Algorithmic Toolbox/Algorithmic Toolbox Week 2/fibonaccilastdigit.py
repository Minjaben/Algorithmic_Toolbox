#Uses Python3

def calc_fib(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)

def fiblast(n):
    F = ([0] * (n + 1))
    F[0] = 0
    F[1] = 1
    for i in range(2,n+1):
        F[i] = (F[i - 1] + F[i - 2])%10
    return (F[n])

n = int(input())

if (n == 0):
    print (0)
else:
    final = (fiblast(n))
    print (final)
