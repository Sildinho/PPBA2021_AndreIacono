# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 8: Estrutura de Dados - Aula: 57 """

# 57. Criando Sets

# set (listas)
    # similar a listas
    # evita itens duplicados
    # nao utiliza index

lista1 = [10, 20, 30, 40, 50, 80, 90]
lista2 = [10, 20, 60, 70]


num1 = set(lista1)
num2 = set(lista2)

print(num1 | num2) # união:  faz a uniao dos grupos e retira os repetidos
print(num1 - num2) # diferença:  retira os repetidos do grupo num1.
print(num1 ^ num2) # diferença simetrica:  retira os repetidos e mostra o restante.
print(num1 & num2) # duplicados:  mostra somente os duplicados.

print(len(num1)) # tamanho do grupo.
print(len(num2)) # tamanho do grupo.



