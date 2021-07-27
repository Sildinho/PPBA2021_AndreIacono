# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 6: Controle de Fluxo - Aula: 33 """

# 33. For Loop - Criando um Retangulo

"""
criar quadrado de 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@

"""

linhas = 6
colunas = 6
simbolo = "#"

for line in range(linhas):
    for column in range (colunas):
        print(simbolo, end="")
    print()



