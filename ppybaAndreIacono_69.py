# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 69 """

# 69. Entendendo List Comprehension com Strings

# list comprehension
    # mais simples de escrever
    # utlizando quando voce precisa criar uma nova lista a partir de uma existente
    # [expressao for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
"""
frutas2 = []

for item in frutas1:
    if 'i' in item:
        frutas2.append(item)
    elif 'k' in item:
        frutas2.append(item)
"""

frutas2 = [item for item in frutas1 if 'n' in item]

print(frutas2)



