"""
Módulo Collections - Counter (Contador)
https://docs.python.org/3/library/collections.html#collections.Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


"""
from collections import Counter

# Exemplo 3

texto = """A Wikipédia é um projeto de enciclopédia multilíngue de licença livre, baseado na web e escrito de 
maneira colaborativa. O projeto encontra-se sob administração da Fundação Wikimedia, uma organização sem fins 
lucrativos cuja missão é "empoderar e engajar pessoas pelo mundo para coletar e desenvolver conteúdo educacional sob 
uma licença livre ou no domínio público, e para disseminá-lo efetivamente e globalmente". Integrando um dos vários 
projetos mantidos pela Wikimedia, os mais de 51 milhões de artigos hoje encontrados na Wikipédia foram escritos de 
forma conjunta por diversos voluntários ao redor do mundo.  """

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrêcia no texto
print(res.most_common(5))
