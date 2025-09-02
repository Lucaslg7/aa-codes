# Algorítimo Guloso

n, m = [int(i) for i in input().split()]
pinos = [int(i) for i in input().split()]

c = 0
for i in range(len(pinos) - 1):
    if pinos[i] == m:
        continue
    if pinos[i] < m:
        dif = m - pinos[i]
        pinos[i] += dif
        pinos[i + 1] += dif
        c += dif
        # while pinos[i] < m:
        #     pinos[i + 1] += 1
        #     pinos[i] += 1
        #     c += 1
    elif pinos[i] > m:
        dif = pinos[i] - m
        pinos[i] -= dif
        pinos[i + 1] -= dif
        c += dif
        # while pinos[i] > m:
        #     pinos[i + 1] -= 1
        #     pinos[i] -= 1
        #     c += 1
            
print(pinos)
    
print(c)
