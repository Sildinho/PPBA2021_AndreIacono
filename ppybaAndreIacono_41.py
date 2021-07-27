# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 7: Funções - Aula: 41 """

# 41. Argumentos Default e Non-default

isso
    # Default = aquele valor definido no parametro. valor padrão definido.
    # Non-Default = aquele que nao é definido no parametro.

# função (parametros)
# a ordem sempre será: Non-Default & Default
def boas_vindas(nome, quantidade = 0):
    print(f'Olá {nome}.')
    print(f'Temos {str (quantidade)} laptops em estoque.')

# chamada de função passando os argumentos
boas_vindas("Marcos", 5)


