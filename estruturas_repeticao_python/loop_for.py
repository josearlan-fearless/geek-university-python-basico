"""
Loop for

Loop -> Estrutra de repetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < limitador; i++) {
    //execução do loop
}

# Em Python
for item in interavel:
    //execucao do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 2, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra, end='')

print('')

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

# range(valor_inicial, valor_final)
OBS: O valor final não é inclusivo.
0
1
2
3
4
5
6
7
8
9
10 -> não

for numero in range(1, 10):
    print(numero)

Enumerate:
(0, 'G'), (1, 'e'), (2, 'e'), (3, 'k')...

for indice, letra in enumerate(nome):
    print(nome[indice])

for valor in enumerate(nome):   -> trás o índice ou o valor ([0 ,1]), ou seja, ou o número do indice ou a letra.
    print(valor[1])

for valor in enumerate(nome):    -> jeito pythonico
    print(valor)

for indice, letra in enumerate(nome):   -> mesma efeito que anterior, porém redundante
    print(f'({indice}, {letra})')

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
OBS: Quando não precisamos desse valor, podemos descartá-lo utilizando um underline.

# nome = 'Geek University'
# lista = [1, 3, 5, 9]
# numeros = range(1, 10)  # Temos que tranformar em uma lista

soma = 0
qtd = int(input("Quantas vezes esse loop deve rodar? "))

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

"""
# Original U+1F60D
# Modificado U0001F60D

emoji = 'U0001F60D'
for num in range(1, 11):
    print('\U0001F607' * num)
