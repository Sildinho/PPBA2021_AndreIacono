# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 62 """

# 62. Looping dentro de um dicionário

# dicionarios
    # utiliza index no formato de keys e values
    #aceita string, integer, float, boolean

aluno = {'nome':'Ana',
        'idade': 16,
        'nota_final': 'A',
        'aprovacao': True}

for x in aluno:
    print(x)

for x in aluno.values():
    print(x)
    
for x in aluno.items():
    print(x)

for keys, values in aluno.items():
    print(f'{keys}: {values}')
