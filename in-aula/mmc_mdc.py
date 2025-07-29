'''
O mmc pode ser dado pela multiplicação dos dois números, divididos pelo mdc deles. mmc(a,b) = (a * b) / mdc(a,b)

O mdc pode ser calculado pela fórmula:
    mdc(a, 0) = a
    mdc(a, b) = mdc(b, a- b)
    
    mdc(a,b):
        if b == 0: return a
        return mdc(b, a-b)
    
    Esse algoritmo tem complexidade linear. 
    Pode ficar O(log n) usando o resto da divisão
    
    mdc(a, b):
        if b == 0: return a
        return mdc(b, a%b)

'''

import time as t

def mdc_n(a,b):
    if b == 0: return a
    return mdc(b, a-b)
    
def mdc(a, b):
    if b == 0: return a
    return mdc(b, a%b)

def mmc(a, b):
    return (a * b / mdc(a,b))

# tempo = t.time()
# print(mdc(10e8, 1))
# print(t.time() - tempo)
# print()
tempo = t.time()
print(mdc_n(10e12, 1))
print(t.time() - tempo)
print()
# tempo = t.time()
# print(mmc(10e9, 1))
# print(t.time() - tempo)
