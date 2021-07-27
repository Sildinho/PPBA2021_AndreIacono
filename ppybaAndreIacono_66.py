# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 66 """

# 66. Função Map em uma lista

# google: built-in functions in python

# map function
    # muito utilizado com listas
    # aplicar um função iterable, por item. (list, tuple, dic, etc...)

lista1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

print(list(map(multi, lista1)))
