# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 6: Controle de Fluxo - Aula: 32 """

# For Loop - Separando Strings

# outer loop
    # inner loop

# modificar : de futebol no mundo para f u t e b o l  n o  m u n d o

palavra = "futebol no mundo!".upper()
palavra = "boston red sox".upper()
palavra = input("Digite uma palavra: ").upper()

for espaco in palavra:
    print(f'{espaco}', end=" ")




