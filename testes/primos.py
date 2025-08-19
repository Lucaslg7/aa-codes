n = int(input())

prim = bytearray[1] * (n + 1)
primps = []

for i in range(2, n + 1):
    if prim[i] == 