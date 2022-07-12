"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.


====================================================================
====================================================================
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda valor: valor > media, dados)

print(list(res))
print(res)
print(type(res))
print(f'Novamente: {list(res)}')

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos
# da memória.
# 007 -> mensagem secreta, ela se auto destroi e limpa a memória
====================================================================
====================================================================
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venzuela']

print(paises)

res = filter(None, paises)

print(list(res))

print((list(filter(lambda pais: pais != "", paises))))
print((list(filter(lambda pais: len(pais) > 0, paises))))
====================================================================
====================================================================
# A diferença entre map(*retorna valores) e filter(*retonar True ou False) é:

# * map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função
# para cada elemento do iterável; Esse retorno sempre será um dado, ou seja um valor contido no
# iterável e processado pelo mesmo com os requisitos da função passada.

# * filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando
# apenas os elementos de acordo com a função. Esse retorno True ou False é que faz com que o
# dado seja selecionado ou não.
====================================================================
====================================================================
# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)
# Filtrar os usuários que estão inativos no Twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)
====================================================================
====================================================================
"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é:' + nome, desde que cada nome tenha
# menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)



