casa_loja1, casa_loja2, loja_loja = [int(i) for i in input().split()]

result = min(casa_loja1 + casa_loja2 + loja_loja,
2 * casa_loja2 + 2 * casa_loja1,
2 * casa_loja1 + 2 * loja_loja,
2 * casa_loja2 + 2 * loja_loja)

print(result)

