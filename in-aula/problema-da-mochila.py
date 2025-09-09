# problema da mochila - dp

def solve(n, c):
    if n < 0 or c <= 0: # caso base
        return 0
    
    if dp[n][c] != -1: return dp[n][c]
    
    if w[n] <= c:
        pegar = v[n] + solve(n - 1, c - w[n])
        nao_pegar = solve(n - 1, c)
        
        dp[n][c] = max(pegar, nao_pegar)
    return dp[n][c]
    

n, c = [int(i) for i in input().split()] # n -> numero de caixas; c -> capacidade da mochila
dp = [[-1] * (c + 1) for _ in range(n)]

w = []
v = []
for i in range(n): # receber os pesos(w) e os valores(v) das caixas
    a, b = [int(i) for i in input().split()]
    w.append(a)
    v.append(b)
    
print(solve(n-1, c))

