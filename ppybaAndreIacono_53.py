# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 53 """

# 53. Agregando Duas listas com o Zip

#  listas
    # armazenar mais de uma informação em variaveis
    # manter a sequencia dos dados em uma variavel

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)

print(list(duas_listas))
