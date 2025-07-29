'''
Podemos encontrar os primos em um intervalo [1,n] em O(n * sqrt(n)), porém dá para melhorar

Crivo de Erastóstenes


'''

def crivo(n):
    nums = [True] * (n+1)
    nums[0] = nums[1] = False
    primos = []
    
    for i in range(2, n+1):
        if not nums[i]: continue
        for j in range(i + i, n+1, i):
            nums[j] = False
        primos.append(i)
    
    return primos
        
print(crivo(2 * 100000))
