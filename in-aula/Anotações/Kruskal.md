# Algoritmo de Kruskal

Resolve o problema da árvore geradora mínima/máxima de um grafo ponderado não-direcionado e conectado.
Queremos encontrar o menor sub-grafo que conecte todos os vértices, com o menor custo (somas das arestas) (árvore geradora mínima)
A árvore geradora mínima possui a menor soma de arestas que permitem que o grafo se mantenha conectado.
// a máxima é o contrário da mínima

Para resolver esse problema, podemos usar DSU. Podemos ir adicionando os vértices ao conjunto, caso uma aresta aponte para um vértice já existente, então não adicionamos.

