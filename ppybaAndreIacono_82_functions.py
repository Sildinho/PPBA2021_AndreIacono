# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 11: Modulos (Arquivos) - Aula: 82 """

# 82. Criando seu primeiro Modulo - functions
# 83. Importando um Modulo
# 85. Aplicando um Modulo


def somar():
    print("função de soma")

def multi():
    print("função de multiplicação")

def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1

    
