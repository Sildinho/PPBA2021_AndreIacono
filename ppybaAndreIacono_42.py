# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 7: Funções - Aula: 42 """

# 42. Print ou Return em Funções

# Functions (Funções):
    # DRY - Don't repeat yourself (Não se repita)
    # Calcula e retorna uma valor.


def cliente1(nome):
    print(f'olá {nome}')


def cliente2(nome):
    return f'olá {nome}'


x = cliente1("Maria")
y = cliente2("José")

print(x)
print(y)
