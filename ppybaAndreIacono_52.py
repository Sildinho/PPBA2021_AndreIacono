# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 52 """

# 52. Verificando itens em uma lista

#  listas
    # armazenar mais de uma informação em variaveis
    # manter a sequencia dos dados em uma variavel

cor_cliente = input("Digite a cor desejada: ")
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('Em estoque.')
else:
    print("Não temos esta cor em estoque.")

