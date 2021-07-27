# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 12: Desafios Python - Aula: 88 """

# 89. Funções (Desafio) - Calculadora para Pintura
# 90. Funções (Solução) - Calculadora para Pintura

"""
criar um programa que calcula a quantida e tinta necesaria para pintar uma parede.
o usuario deverá fornecer as seguintes informações: rendimento, altura e larguraself.
o programa deve mostrar na tela a mensagem: 'voce necessita de x latas de tinta'.

"""

def quant_tinta(rend, altu, largu):
    metro_quadrado = altu*largu
    quant_necessaria = metro_quadrado / rend
    print(f'voce necessita de {quant_necessaria} latas de tinta.')

rend = float(input("Digite o rendimento esperado da tinta: "))
altu = float(input("Digite altura da parede: "))
largu = float(input("Digite altura da parede: "))

quant_tinta (rend, altu, largu)

