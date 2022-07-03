"""
Tipo String

Em Python, um dado é considerado do tipo String sempre que:

- Estiver entre aspas simples -> 'uma string', 'a', '234', 'True', '42.3'

- Estiver entre aspas duplas -> "uma string", "a", "234", "True", "42.3"

- Estiver entre aspas simples triplas -> '''uma string''', '''a''', '''234''', '''True''', '''42.3'''

nome = 'Geek university'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

nome = 'Geek University'
print(nome.upper())

print(nome.lower())

print(nome.split()) -> Transforma em uma lista de string


nome = 'Geek University'
print(nome[0:4])  # Slice de String

print(nome[5:15])  # Slice de String

print(nome.split())
# [ 0,       1]
# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])

"""
# - Estiver entre aspas duplas triplas ->  """uma string""", """a""", """234""", """True""", """42.3"""

# nome = """Angelina
# Jolie"""
# print(nome)
# print(type(nome))

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   0,  11,  12,  13,  14 ]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

nome = 'Geek University'
"""
[::-1]  -> Começa do primeiro elemento, vai até o útimo elemento e inverta
"""
print(nome[::-1])  # Inversão da string Pythônico
print(nome.replace('e', 'i'))
print(type(nome))

texto = "socorram me subino onibus em marrocos"  # Um texto chamado de palíndromo
print(texto)
print(texto[::-1])

nome = 'ana'  # Palíndromo
print(nome)
print(nome[::-1])
