# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 6: Controle de Fluxo - Aula: 26 """

# 26. Operador Ternário

idade = 2021 - int(input("Digite o ano do seu nascimento: "))

# voto permitido "se" idade for igual ou maior que 16. "se nao" o voto nao é permitido.
resultado = "voto permitido" if idade >= 16 else "voto nao permitido"

print(resultado)
