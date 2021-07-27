# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 11: Modulos (Arquivos) - Aula: 82 """

# 82. Criando seu primeiro Modulo - main
# 83. Importando um Modulo
# 85. Aplicando um Modulo

# formar de importar modulos com import e/ou from

# import ppybaAndreIacono_82_functions as functions

from ppybaAndreIacono_82_functions import find_index

list1 = ['a', 'b', 'c', 'd', 'e', 'f']

var1 = find_index(list1, 'f')
# var1 = functions.find_index(list1, 'b')

print(var1)


"""
# acessando packages
from items.cadastro import cliente

functions.somar()
functions.multi()
cliente()

"""
