# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 49 """

# 49. Concatenando listas

# listas
    # armazenar mais de uma informação em variaveis
    # manter a sequencia dos dados em uma variavel

# concatenando listas
numeros = [1,2,3,4]
print(numeros[2])

itens = [['item1', 'item2'], ['item3', 'item4']]

print(itens[1][0])
print(itens[1][1])

print("** "*15)
# concatenando listas

brasil = [['rio de janeiro', 'sao paulo', 'minas gerais', 'espirito santo'], ['paraná', 'santa catarina', 'rio grande do sul'], ['goias', 'mato grosso', 'mato grosso do sul']]

print((brasil[0][3]).title().strip())
print((brasil[1][1]).title().strip())
print((brasil[2][2]).title().strip())
print(brasil[1])
