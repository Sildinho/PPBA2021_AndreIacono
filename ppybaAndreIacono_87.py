# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 12: Desafios Python - Aula: 87 """

# 87. If, Elif, Else (Desafio) - Ponto do Steak
# 88. If Else (Solução) - calculo pintura (tinta na parede)


"""
criar um programa que dependendo da tempratura (em celsius) do steak ele retorna o ponto de cozimento. o usuario deverá fornecer a temperatura.

Temperaturas - cozimento
menor que 48 - crua
120°F ou 48°C - rare (selada)
130°F ou 54°C - medium rare (ponto pra mal)
140°F ou 60°C - medium (ponto)
150°F ou 65°C - medium well (ponto pra bem)
160°F ou 71°C - well done (bem passada)
"""

ponto_carne = float(input("Digite a temperatura da carne: "))

"""
if ponto_carne < 48:
    print("Tá crua")
elif ponto_carne >= 48 and ponto_carne < 54:
    print("rare (selada)")
elif ponto_carne >= 54 and ponto_carne < 60:
    print("medium rare (ponto pra mal)")
elif ponto_carne >= 60 and ponto_carne < 65:
    print("medium (ponto)")
elif ponto_carne >= 65 and ponto_carne < 71:
    print("medium well (ponto pra bem)")
else:
    print("well done (bem passada)")

"""

if ponto_carne < 48:
    print("Tá crua")
elif ponto_carne in range(48, 53):
    print("rare (selada)")
elif ponto_carne in range(54, 59):
    print("medium rare (ponto pra mal)")
elif ponto_carne in range(60, 64):
    print("medium (ponto)")
elif ponto_carne in range(65, 70):
    print("medium well (ponto pra bem)")
else:
    print("well done (bem passada)")
