# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 58 """

# 58. Funções em sets

# set (listas)
    # similar a listas
    # evita itens duplicados
    # nao utiliza index

lista1 = [1, 2, 3, 4, 5, 6]
print(lista1)
print(type(lista1))

lista1 = set([1, 2, 3, 4, 5, 6]) # mudando o tipo para set.
print(lista1)
print(type(lista1))

print("**  *  ***  "*10)

s1 = {1, 2, 3, 4, 5, 6}
print(s1)

s1.add(7) # para adicionar somente 01 item.
print(s1)

s1.update({7, 8, 9, 10}) # para adicionar multiplos itens.
print(s1)

s1.remove(10) # para remover 01 item.
print(s1)

s1.discard(9) # para descartar 01 item. pode remover mesmo se ainda nao existir na lista.
print(s1)

print(type(lista1))
print(type(s1))





