# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 55 """

# 55. Entendendo sobre Tuples

#  listas
    # armazenar mais de uma informação em variaveis
    # manter a sequencia dos dados em uma variavel
    # nao podem ser alteradas (imutavel)

# a diferença é lista usa colchetes e tuplas usam parenteses. tem mais coisas.
# append: em tuple nao funciona.

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

cores_list.append('roxa')
# cores_tuple.append('roxa') --> 'tuple' object has no attribute 'append'

print(type(cores_list))
print(type(cores_tuple))

print(cores_list)
print(cores_tuple)
