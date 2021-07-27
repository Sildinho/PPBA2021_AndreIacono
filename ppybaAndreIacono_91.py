# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 12: Desafios Python - Aula: 91 """

# 91. Sets (Desafio) - Filtrando funcionários em uma empresa
# 92. Sets (Solução) - Filtrando funcionários em uma empresa

"""
desafio com sets

criar um programa que gera 03 listas de acordo com a necessidade logo abaixo:

lista1 = funcionario que tem carro e trabalham a noite.
lista2 = funcionario que tem carro e trabalham de dia.
lista3 = funcionario que nao tem carro.

"""

funcionario = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
truno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

funcionario = set(funcionario)
turno_dia = set(turno_dia)
turno_noite = set(truno_noite)
tem_carro = set(tem_carro)
print("\nComo eu fiz:")
print(f'funcionario que tem carro e trabalham a noite: {tem_carro & turno_noite}')
print(f'funcionario que tem carro e trabalham de dia: {tem_carro & turno_dia}')
print(f'funcionario que nao tem carro: {funcionario - tem_carro}')

print("\nComo ele fez:")
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)
lista3 = set(funcionario).difference(tem_carro)
print(lista3)
