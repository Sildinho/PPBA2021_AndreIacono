# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 9: Erros - Aula: 73 """

# 73. Trabalhando com o Try e Except com uma lista

# erros (try except)
    # excelentes para testes
    # nao realiza o 'stop' no programa
    # mensagens customizadas quando 

try:
    letras = ['a','b','c']
    print(letras[3])

except IndexError:
    print("Deu ruim")