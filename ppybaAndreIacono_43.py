# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 7: Funções - Aula: 43 """

# 43. Vários argumentos xargs com números

# Functions (Funções):
    # DRY - Don't repeat yourself (Não se repita)
    # varios argumentos (xargs)
    # criar uma função que soma varios numeros é preciso um loop
    

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

#print(soma(2,3,4,7))
x = soma(2,3,4,7)
print(x)


