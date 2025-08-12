from collections import deque

n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

parada = deque(a)

passageiros = 0
onibus = 0
while True:
    if len(parada) == 0:
        break
    if passageiros < m:
        pass
        

print(onibus)

