"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma ateatória,
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)
OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Exemplo Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

for num in range(1, 11):
    print(num)

# Exemplo Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

for num in range(0, 50, 5):
    print(num)

# Exemplo Forma 4
range(valor_inicial, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

for num in range(10, -1, -1):
    print(num)

OBS: Para imprimir o range precisamos converte-lo em uma lista por exemplo:
lista = list(range(11))
print(lista)
resultado seria o seguinte: -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


