def union(u, v):
    u = find(u) # encontrar o pai de u
    v = find(v) # encontrar o pai de v
    
    if u != v:
        size[v] += size[u]
    parents[u] = v
    
# Path Compression
def punion(u, v):
    u = pfind(u) # encontrar o pai de u
    v = pfind(v) # encontrar o pai de v
    
    if u != v:
        size[v] += size[u]
    parents[u] = v

def find(v):
    if v == parents[v]: # se ele for o proprío pai, acaba a recursão
        return v
    return find(parents[v]) # se houver um pai diferente dele mesmo, ele continua


# se fizer vários finds em um grafo com muitos vertices, é muito lento. Como otimizar?
# Path Compression
def pfind(v):
    if v == parents[v]: # se ele for o proprío pai, acaba a recursão; se houver um pai diferente dele mesmo, ele continua
        return v
    parents[v] = find(parents[v]) # ao passar em cada elemento, já marcamos ele com o parent, para quando outro find for realizado, não precisarmos passar de novo
    return parents[v] 


n = int(input())

parents = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]

t = int(input())
for i in range(t):
    q = int(input())
    
    if q == 1:
        u, v = [int(i) for i in input().split()]
        punion(u, v)
    elif q == 2:
        v = int(input())
        print(size[v])
    elif q == 3:
        v = int(input())
        print(pfind(v))



