# Aritmética Modular

- Soma Modular

c = (a + b) % M

Ao invés de tirar o módulo da soma, podemos tirar o módulo de a e b antes de somarmos, para evitar trabalhar com números muito grandes.

Então, temos:

a %= M
b %= M
c = (a + b) % M


- Subtração Modular

c = (a - b) % M

Podemos fazer a mesma coisa da soma, tirando o módulo de a e b, subtraindo e aplicando o modulo depois

a %= M
b %= M
c = (a - b) % M


- Multiplicação Modular

c = (a * b) % M

Aplicando a lógica anterior, podemos aplicar o módulo em a e b e multiplicar pelo módulo no final

a %= M
b %= M
c = (a * b) % M


- Divisão Modular


