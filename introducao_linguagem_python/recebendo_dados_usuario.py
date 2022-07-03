"""
Recebendo dados do usuário

input() Todo dado recebido via input é do tipo String
Em Python, string é tudo o que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# - Aspas duplas triplas -> """Angelina Jolie"""

# Entrada de dados
# print("Qual o seu nome? ")
# nome = input()  # -> Input -> Entrada

nome = input("Qual o seu nome? ")

# Exemplo de print antigo do python 2.x
print('Seja Bem-vindo(a) %s' % nome)

# print('Qual a sua idade? ')
# idade = input()

idade = int(input('Qual a sua idade? '))  # Cast feito logo aqui no momento da entrada

# Exemplo de print antigo do python 2.x
# print('A(o) %s tem %s anos de idade' % (nome, idade))
# Processamento

# Saída de dados
# Exemplo de print modernos criados a partir das versões 3.x do python
print('O(a) {0} tem {1} anos de idade'.format(nome, idade))

# Exemplo de print mais atual do python 3.x
print(f'{nome} tem {idade} anos de idade')
# print(f'A {nome} nasceu em {2022 - int(idade)}')
print(f'O(a) {nome} nasceu em {2022 - idade}')

"""
# int(idade) => cast
Cast é a 'conversão' de um tipo de dado para outro
"""
