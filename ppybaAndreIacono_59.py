# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 59 """

# 59. Sets com strings

# set (listas)
    # similar a listas
    # evita itens duplicados
    # nao utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)

set5 = set1.difference(set3)

set6 = set1.intersection(set2)

set7 = set1.symmetric_difference(set3)

print(set4)
print(set5)
print(set6)
print(set7)
