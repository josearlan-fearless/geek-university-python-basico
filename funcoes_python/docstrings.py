"""
Documentando funcão com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python utilizando
a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help()

"""
# print(help(print))
# Exemplos

def diz_oi():
    """Uma função simples que retorna a string Oi!"""
    return 'Oi!'


print(diz_oi())

print(help(diz_oi))


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'número' ou o 'número à potência informada.
    :param numero: Número que esperamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'número por 'potência'.
    """
    return numero ** potencia










