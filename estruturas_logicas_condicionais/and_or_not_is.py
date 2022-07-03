"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not

Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o and, ambos os valores precisam ser True
Para o or, um ou outro valor precisam ser True
Para o not, o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
Para o is, o valor é comparado com um segundo valor.
"""

ativo = False
logado = True
if ativo or logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu email")

if not ativo:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
else:
    print("Bem-vindo usuário")

print(not False)

if ativo is True:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu email")

if ativo:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, cheque seu email")


print(ativo is False)
