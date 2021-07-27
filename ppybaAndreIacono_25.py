# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 6: Controle de Fluxo - Aula: 25 """

# 25. Operadores lógicos

renda_acima_5mil = True
nome_limpo = False

# primeiro banco
if renda_acima_5mil and nome_limpo:
    print("banco 1 = Aprovado")
else:
    print("banco 1 = Negado")

# segundo banco
if renda_acima_5mil or nome_limpo:
    print("banco 2 = Aprovado")
else:
    print("banco 2 = negado")