n = int(input())

sieve = bytearray(b'\x01') * (n + 1)   # 1 = potencialmente primo
sieve[0:2] = b'\x00\x00'               # 0 e 1 não são primos
limite = int(n ** 0.5)

for p in range(2, limite + 1):
    if sieve[p]:                       # se ainda marcado como primo
        inicio = p * p                 # comece em p²
        passo = p
        sieve[inicio:n+1:passo] = b'\x00' * (((n - inicio) // passo) + 1)
        
primos = [i for i in range(n + 1) if sieve[i]]

if sieve[n]:
    print(n)
elif n % 2 == 0 and sieve[n // 2]:
    print(n // 2, n // 2)
elif n % 3 == 0 and sieve[n // 3]:
    print(n // 3, n // 3, n // 3)
if sieve[(n // 2) // 2]:
print(  )
else:
    for i in primos[2::]:
        if sieve[n // i]:
            aux = n - i
            if sieve[aux]:
                if (i + aux) == n:
                    print(i, aux)
                    break
            else:
                if (n // i, aux // 2, aux // 2) == n:
                    print(n // i, aux // 2, aux // 2)
                    break
# 18 // 2
# 9
# 18 // 3
# 6
# 18 // 5
# 3

# 18 - 5
# 13
# 5

# 27 // 2
# 13
# 27 - 13
# 14
# 14 // 2
# 7 7

29
13 13