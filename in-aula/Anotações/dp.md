# Programação dinâmica (DP)

Consiste em identificar uma função de recorrência em um algoritmo.
Para isso, definimos o caso base f(0) e depois definimos o passo indutivo f(n) = f(n - k) + n

Para otimizar, guardamos o resultado de cada f(n - k), afim de que, caso ele se ocorra novamente, não precisemos calcular novamente.

Formas de resolver dp

- Bottom-up
    iterativo, vamos do caso base a n

- top-down
    recursivo, começamos de n e vamos descendo a árvore até o caso base
