"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis; Isso significa que ao se criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

print(type(()))

========================================================================================
========================================================================================

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# CUIDADE 2: Tuplas com 1 elemento

tupla3 = (4)  # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4, )  # Isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parênteses.
(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla
========================================================================================
========================================================================================

# Podemos gerar uma tupla dinamicamente com o range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))
========================================================================================
========================================================================================
# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera (ValueError) se colocarmos un número diferente de elementos para desempcacotar.
# Métodos para adição e remoção de elentos nas tuplas não existem, dado o fato das tuplas serem imutáveis.
========================================================================================
========================================================================================
# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho

# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
tupla = (1, 2, 3, 4, 5, 6, 'b')  # Aqui daria error em sum(), max(), min(), pois temos um valor
diferente de inteiro ou real.

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
========================================================================================
========================================================================================
# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla2)
print(tupla1)

tupla1 = tupla1 + tupla2  # Tuplas são imutáveis, mas podemos sobrescrever seus valores.
print(tupla1)

========================================================================================
========================================================================================
# Verificar se determinado elemento está contigo na tupla.

tupla = (1, 2, 3)

print(3 in tupla)
========================================================================================
========================================================================================
# Iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
========================================================================================
========================================================================================
# Contando elementos dentro de uma tupla.

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek University')

print(escola)

print(escola.count('e'))
========================================================================================
========================================================================================
# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com o while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice um elemento está na tupla
print(meses.index('Junho', 6))

# OBS: Caso o elemento não exista será gerado ValueError.

# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])

========================================================================================
========================================================================================
# Por quê utilizar tuplas?

# - Tuplas são mais rápidas que listas.
# - Tuplas deixam seu código mais seguro.
# * Isso porque trabalhar com elementos imutáveis trás segurança para o código
========================================================================================
========================================================================================

"""
# Copiando uma tupla para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o processo de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
