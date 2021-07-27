# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 63 """

# 63. Visualizando Itens, Keys e Values

# dicionarios
    # utiliza index no formato de keys e values
    #aceita string, integer, float, boolean

aluno = {'Nome':'Ana',
        'Idade': 16,
        'Nota_final': 'A',
        'Aprovacao': True,
        'Materias': ['Fisica', 'Matematica', 'Ingles']}

print(aluno)
print(aluno.get('Materias'))
print(len(aluno))
print(aluno.items())
print(aluno.keys())
print(aluno.values())
