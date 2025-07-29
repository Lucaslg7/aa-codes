import math

# Como encontrar todos os divisores de um numero n

# Solução trivial

n = int(input())
c = 0
for i in range(1, n):
    if n % i == 0:
        c += 1
        
print(c)

# Solução eficiente
# Erro

div = []
for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0:
        div.append(i)

    if n // i != i:
        div.append(n // i)
        
print(div)