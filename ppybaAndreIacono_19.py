# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 4: Python Basico - Aula: 19 """

# formated strings + metodos

# O marcos silva é um excelente [programador] # nem sei se existe.

nome = ("marcos").title().strip()
sobrenome = ("silva").title().strip()
profissao = ("programador").upper().strip()

# texto = "O "+ nome + " "+sobrenome +" é um excelente ["+profissao+"]." # nem sei se existe.

# print(texto)

print(f'O {nome} {sobrenome} é um excelente [{profissao}].') # usando string formatada.

print("O " + nome +" "+ sobrenome + " é um excelente ["+profissao+"].")

#print("O " + nome.title().strip() +" "+ sobrenome.title().strip() + " é um excelente ["+profissao.upper().strip()+"].")




