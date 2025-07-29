mod = 10**9 + 7

# Sem exponenciação rápida 

x = 1
for i in range(10**4):
    x = (x % mod) * (2 % mod)
print(x)

# Com exponenciação rápida 

# def bin_pow_2(a: int, n: int) -> int:
#     if n == 0:
#         return a
    
#     return (bin_pow_2(a, n // 2) % mod) ** 2

def bin_pow_2(a: int, b: int, mod) -> int:
    if b == 1: return a
    
    x = bin_pow_2(a, b // 2, mod)
    x *= x % mod
    
    if b % 2 == 1:
        x *= a % mod
    
    return x

print(bin_pow_2(2, 10**4, mod))