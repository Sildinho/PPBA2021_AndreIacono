# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 65 """

# 65. Lambda dentro de uma função

# lambda function
    # é um função (pequena) sem nome
    # pode ter varios argumentos mas coment 1 expressao
    # muito utilizada dentro de outras funções
    # codigos mais "clean"


def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4
    # return func2(x * 4)
print(somar(2))


