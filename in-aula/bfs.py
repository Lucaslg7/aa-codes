from collections import deque

n = 10
adjacencia = [[] for i in range(n + 1)]
for i in range(n):
    u, v = [int(i) for i in input().split()]
    adjacencia[u].append(v)
    adjacencia[v].append(u)
    
visitados = [False] * n 
processados = deque()