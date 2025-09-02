# exemplo das moedas (incompleto)
INF = 1e9

def solve(moedas, valor):
    if dp[moedas][valor] != -1: return dp[moedas][valor]
    
    if valor == 0:
        return 0
    if moedas == 0:
        return 10**18
    
    nao_pega = solve(moedas-1, valor)
    pega = solve(moedas, valor - coins[moedas - 1]) + 1 if valor >= coins[moedas - 1] else INF
    dp[moedas][valor] = min(nao_pega, pega)
    return dp[moedas][valor]
    
    

n = int(input())

print(solve(4, n))
