# União de Conjuntos Disjustos

Temos n conjuntos distintos, onde cada conjunto guarda um número.
Podemos fazer estas operações:
    - Escolher dois elementos e mesclar os conjuntos onde eles se encontram, formando um novo conjunto.
    - É dado um número u, e você deve olhar em qual conjunto esse u está e calcular o número de elementos desse conjunto.
    - Verificar se u e v estão no mesmo conjunto.

# Union Find

Estrutura de dados usada para armazenar um conjunto de elementos agrupados em subconjuntos disjuntos.
Possui duas operações:
    - union(u, v) -> une os dois conjuntos onde u e v estão
    - find(v) -> retorna o patriarca do conjunto onde v está

-> Como funciona?
    Cada conjunto pode ser representado por um único elemento, que será denominado parent.
    Para unir dois conjuntos, criamos uma conexão entre os dois conjuntos (grafo).
    Para isso, criaremos um array de ponteiros para os patriarcas.
    Para saber se um número está num conjunto, verificamos se eles tem o mesmo parent

# Path Compression

Técnica usada para ligar diretamente um elemento de um determinado conjunto ao seu parent.

1 - 2 - 3 - 4
ligaríamos o 1 diretamente ao 4

Para melhorar ainda mais essa técnica, ligamos os elementos que estão no caminho ao parent.

1 - 2 - 3 - 4
não ligamos somente o 1 ao 4, mas ligamos o 2 ao 4 