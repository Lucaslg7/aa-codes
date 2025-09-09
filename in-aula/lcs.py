# LCS - Longest Common Sequence
# Qual a maior subsequencias entre duas strings?

def solve(i, j): # i -> prefixo da primeira str; j -> prefixo da segunda str
    iguais = dif = pega_i = nao_pega_i = 0
    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1: return dp[i][j]
    
    if s1[i] == s2[j]:
        iguais = solve(i - 1, j - 1) + 1
    else:
        dif = solve(i - 1, j - 1)
        
    pega_i = solve(i, j - 1)
    nao_pega_i = solve(i - 1, j)
    
    dp[i][j] = max(iguais, dif, pega_i, nao_pega_i)
    return dp[i][j]

s1 = input()
s2 = input()

dp = [[-1] * len(s2) for _ in range(len(s1))]

print(solve(len(s1) - 1, len(s2) - 1))
