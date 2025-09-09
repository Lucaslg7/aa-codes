# Programação Dinâmica II

- Problema da mochila

w = [lista de pesos]
v = [lista de valores]
f (n, c) = max(f(n - 1, c), (v[w] + f(n - 1, c - v[w])))

Casos Base:
f (n, x) = 0, se x <= 0
f (0, c) = 0

- LCS - Longest Common Sequence
Qual a maior subsequencias entre duas strings?

Caso base
if i < 0 or j < 0:
    return 0

if s1[i] == s2[j]:
    iguais = solve(i - 1, j - 1) + 1
else:
    dif = solve(i - 1, j - 1)
    
pega_i = solve(i, j - 1)
nao_pega_i = solve(i - 1, j)
