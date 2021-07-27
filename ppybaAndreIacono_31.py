# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 6: Controle de Fluxo - Aula: 31 """

# 31. For Loop - Nested loops (for loop dentro de for loop)

# outer loop
    # inner loop
"""
for numero1 in range (1,3):
    print((f'\n{numero1} - está no loop de fora').upper())
    
    for numero2 in range (1,4):
        print(f'\t{numero2} - está loop de dentro')
"""

for numero1 in range (1,4):
    print((f'\nProduto - {numero1}').upper())
    
    for numero2 in range (1,5):
        print(f'\t{numero2} - está loop de dentro')



