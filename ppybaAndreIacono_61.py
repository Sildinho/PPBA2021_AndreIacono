# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 61 """

# 61. Atualizando itens no dicionário

# dicionarios
    # utiliza index no formato de keys e values
    #aceita string, integer, float, boolean

aluno = {'nome':'Ana',
        'idade': 16,
        'nota_final': 'A',
        'aprovacao': True}

aluno.update({'nome':'José', 'nota_final': 'B'})
print(aluno)

aluno.update({'Endereço':'221b Baker st'})
print(aluno.get('Endereço', 'Não encontrado')) # se encontra ok senao "nao encontrado"
print(aluno.get('Documento', 'Não encontrado')) # se encontra ok senao "nao encontrado"

del aluno['idade']
#aluno.pop('idade') tentar usar pop se precisar da info depois.
print(aluno)
print(aluno.get('idade', 'Não encontrado'))
