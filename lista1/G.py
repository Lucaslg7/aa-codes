def cont_abc(s, n, m):
    cont = 0
    for j in range(m, n - 2):
        if s[j] + s[j+1] + s[j+2] == 'ABC':
            cont += 1
    return cont

n, q = [int(i) for i in input().split()]
s = list(input())
cont_init = cont_abc(s, n, 0)

for i in range(q):
    x, c = input().split()
    x = int(x)
    antes_troca = cont_abc(s, x - 3, x + 2)
    s[x-1] = c
    depois_troca = cont_abc(s, x - 3, x + 2)

    if depois_troca > antes_troca: 
        cont_init += 1
    elif depois_troca < antes_troca:
        cont_init -= 1
    
    print(cont_init)