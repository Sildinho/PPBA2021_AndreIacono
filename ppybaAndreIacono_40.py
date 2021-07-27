# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 7: Funções - Aula: 40 """
# 40. Parâmetros e Argumentos em uma função

"""
# funções
def boas_vindas_Marcos():
    print("Olá Marcos")
    print("Temos 5 laptops em estoque.")

def boas_vindas_Ronaldo():
    print("Olá Ronaldo")
    print("Temos 4 laptops em estoque.")

def boas_vindas_linda():
    print("Olá Linda")
    print("Temos 2 laptops em estoque.")

boas_vindas_Marcos()
boas_vindas_Ronaldo()
boas_vindas_linda()
"""

# função (parametros)
def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str (quantidade)} laptops em estoque.')


# chamada de função passando os argumentos
boas_vindas("Marcos", 5)
boas_vindas("Ronaldo", 4)
boas_vindas("LInda", 2)
