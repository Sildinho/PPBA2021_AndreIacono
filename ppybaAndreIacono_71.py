# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 71 """

# 71. Lista e Generator Expressions

# generator expressions
    # uma forma mais rapida para listas, dicionarios e tecself.
    # menos memoria alocada
    # valores em bytes

from sys import getsizeof

"""
numeros = [x * 10 for x in range(5)]

print(numeros)
"""
# pior
numeros = [x * 10 for x in range(11)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print("\n"+"*  **  "*10 + "\n")

# melhor
numeros = (x * 10 for x in range(11))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))


