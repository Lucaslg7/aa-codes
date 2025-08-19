# ainda nao esta funcionando, mas a função desisjkra esta correta

import heapq
import math

def desisjskra(edges, source):
    dist = [math.inf] * (n + 1)
    dist[source] = 0
    pq = [(0, source)]
    
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u, w in edges[v]:
            if d + w >= dist[u]:
                dist[u] += d + w
                heapq.heappush(pq, (dist[u], u))
    
    return dist
    
    
n, m = [int(i) for i in input().split()]

edges = [[] for i in range(n + 1)]

for i in range(m):
    w, u, v = [int(i) for i in input().split()]
    edges[u].append((w, v))
    edges[v].append((w, u))
    
print(desisjskra(edges, 1))

