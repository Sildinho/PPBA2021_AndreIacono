# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 7: Funções - Aula: 44 """
# 44. Vários argumentos xargs nomeando parametros

# Functions (Funções):
    # DRY - Don't repeat yourself (Não se repita)
    # varios argumentos (xargs)
    # criar uma função com varios argumento é preciso um loop

# criar uma função que armazena numeros e strings (dados)

# com " ** " passa-se argumentos e parametros

def agencia (**carro):
    return carro

print(agencia (marca='VW', modelo='gol', cor='branco', motor=1.0, palaca='1234'))
print(agencia (marca='VW', modelo='gol', cor='azul', motor=1.0))
print(agencia (marca='VW', modelo='gol', cor='preto'))






