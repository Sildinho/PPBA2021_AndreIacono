# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 7: Funções - Aula: 39 """

# 39. Criando uma função de soma

# Functions (Funções):
    # DRY - Don't repeat yourself (Não se repita)
"""
numero1 = 10
numero2 = 5
resultado1 = numero1 + numero2

print(f'resultado1 = {resultado1}') """

# funções
def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2

    print(f'resultado = {resultado}')


def somar_dois_numeros2():
    numero1 = 10
    numero2 = 2
    resultado = numero1 + numero2

    print(f'resultado2 = {resultado}')

# chamada de função sem passagem de argumentos
somar_dois_numeros()
somar_dois_numeros2()
