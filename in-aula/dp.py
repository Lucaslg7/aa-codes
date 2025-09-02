# exemplo da escada

import sys
sys.setrecursionlimit(10**8)
sys.set_int_max_str_digits(10**8)

n = int(input())

calculado = [-1] * (n + 1)
def dp(n):
    if calculado[n] != -1:
        return calculado[n]
    else:
        if n <= 2:
            calculado[n] = n
            return n
        calculado[n] = dp(n - 1) + dp(n - 2)
        return calculado[n]


print(dp(n))
