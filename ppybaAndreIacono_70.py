# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 46 """

# 70. Entendendo List Comprehension com números

# list comprehension
    # mais simples de escrever
    # utlizando quando voce precisa criar uma nova lista a partir de uma existente
    # [expressao for iten in itens]

"""   
valores = []

for x in range(6):
    valores.append(x * 10)

print(valores)

"""

valores = [x * 10 for x in range(11)]

print(valores)
