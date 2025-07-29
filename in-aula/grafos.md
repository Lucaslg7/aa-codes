# Representação de grafos não-ponderados

- Matriz de Adjacência

Matriz n x n, onde n é o número de vértices
Se A(i,j) for igual a 0, então significa que não há uma aresta do nó i para o nó j e vice-versa.
Essa abordagem serve tanto para grafos direcionais e não-direcionais

- Lista de Adjacência

Lista em que cada posição vai guardar outra lista com os vizinhos de um determinado vértice.

Ex. direcionado:
[[], [2, 3], [1, 4]]
OBS: Não há vértice 0

1 é ligado ao 2 e ao 3
2 é ligado ao 1 e ao 4

Ex. não-direcionado
[[], [2, 3], [1, 4], [1], [2]]

1 é ligado ao 2 e ao 3
2 é ligado ao 1 e ao 4
3 é ligado ao 1
4 é ligado ao 2

# Representação de grafos ponderados

Neste caso, se usarmos a matriz, ao invés de usarmos um booleano para marcar a existência da aresta, guardaremos o peso. Se houver peso, é porque a aresta existe e o valor é o peso daquela aresta

No caso da lista, guardaremos um par contendo a ligação e o peso da aresta.

Ex. lista de adjacência
[
    [], 
    [(2, 6), (3, 8)], 
    [(1, 2), (4, 9)]
]

# Como percorrer um grafo?

- DFS (Busca em Profundidade)
    Algoritmo recursivo, percorre um caminho enquanto consegue

Uso para saber se há um caminho possível dado um determinado vértice. Não funciona para encontrar a menor distância entre vértices

- BFS (Busca em Largura)
    Algoritmo que utiliza de uma fila para explorar o grafo de forma abrangente

Usado para descobrir as menores distâncias de um vertice até outro. Não funciona para grafo ponderado (usar djiskra)