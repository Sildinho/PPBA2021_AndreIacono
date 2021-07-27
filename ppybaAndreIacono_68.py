# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 68 """

# 68. Função Filter

# filter function
    # muito utilização com listas
    # aplicar uma função a um iterable, filtrando os items. (list, tuple, dic etc...)

valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x>20
print("Usando map com e sem lambda")
print(list(map(remover20,valores)))

print(list(map(lambda x: x > 20,valores)))

print("\n"+"**  *  "*15)
print("Usando filter com e sem lambda")
print(list(filter(remover20,valores)))

print(list(filter(lambda x: x > 20,valores)))






