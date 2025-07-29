n, x = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

# usar 2 ponteiros; o r anda se a soma for maior; com isso, a soma fica menor e o l anda
    
soma = 0 # Ponteiro direita
r = 0
for l in range(n):
    r = max(r, l)
    while soma + nums[r] < x and r < n:
        soma += nums[r]
        r += 1

    if soma == x:
        print('Sim')
        exit(0)
    soma -= nums[l]

print('Não')
    