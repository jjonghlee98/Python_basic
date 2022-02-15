def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

def fib(n):
    f = [0, 1]
    for _ in range(2, n+1, 2):
        f[0] += f[1]
        f[1] += f[0]
    return f[n%2]

n = int(input('n >> '))
print(f'fibonacci({n}) = {fib(n)}')
