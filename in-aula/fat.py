import sys

sys.setrecursionlimit(10000)

M = 10**9 + 7

def fat(n):
    if n == 1: 
        return 1 % M

    return n * fat((n - 1) % M)

print(fat(1000))