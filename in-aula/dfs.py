def dfs(v: int) -> bool:
    for i in adjacencia[v]:
        if not visitados[i] and len(adjacencia[i]) > 0:
            visitados[i] = True
            dfs(i)
   
   
def dfss(v):
    visitados[v] = True
    for vizinho in adjacencia[v]:
        if visitados[vizinho]: continue
        dfss(vizinho)
n = 10
adjacencia = [[] for i in range(n + 1)]
for i in range(n):
    u, v = [int(i) for i in input().split()]
    adjacencia[u].append(v)
    adjacencia[v].append(u)
    
visitados = [False] * n 
visitados[1] = True
dfs(1)
print(visitados)

visitados = [False] * n 
dfss(1)
print(visitados)