# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 56 """

# 56. Trabalhando com Arrays

# Google: array - efficient arrays of numeric values

"""
u = strring
i = inteiro
f = float
"""

# array (matriz)
    # similar a listas
    # melhor performance

from array import array
letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2, 4.3]

print(letras)
print(numeros_i)
print(numeros_f)

print("***  *  "*10)

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2, 4.3])

print(letras)
print(numeros_i)
print(numeros_f)
