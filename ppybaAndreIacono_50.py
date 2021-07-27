# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 50 """

# 50. Extraindo variáveis de Listas

# unpacking listas
    # armazenar mais de uma informação em variaveis
    # manter a sequencia dos dados em uma variavel

produtos = ['arroz', 'feijão', 'laranja', 'banana', 4, 5, 6, 7]

item1, item2, item3, *outros = produtos

print(item1)
print(item2)
print(item3)
print(outros)

