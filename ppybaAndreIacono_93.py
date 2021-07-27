# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 12: Desafios Python - Aula: 93 """

# 93. If Elif (Desafio) - Calculo de BMI

"""
Calculo de IMC - ìndice de Massa Corporal

altra em cm:
peso em Kg:

magrelo - menor que 18.5 
normal - entre 18.5 e 24.9
sobrepeso - entre 25.0 e 29.9
obsidade - entre 30.0 e 39.9
obsidade grave - maior que 40.0
"""

# colocar um loop aqui antes de finalizar.
try:
    altura = int(input("\nDigite sua altura em centimetros: "))

except ValueError:
    print("\nDigite somente numeros.\n")

try:
    peso = int(input("\nDigite seu peso: "))

except ValueError:
    print("\nDigite somente numeros.\n")

finally:

    imc = peso / (float(altura * altura)/10000)
    # print(imc)

    if imc < 18.5:
        print(f'Seu IMC é {imc:.2f}')
        print("Magrelo")

    elif imc >= 18.5 and imc < 25:
        print(f'Seu IMC é {imc:.2f}')
        print("Normal")

    elif imc >= 25 and imc < 30.0:
        print(f'Seu IMC é {imc:.2f}')
        print("sobrepeso")

    elif imc >= 30 and imc < 40.0:
        print(f'Seu IMC é {imc:.2f}')
        print("obsidade")

    else:
        print(f'Seu IMC é {imc:.2f}')
        print("obsidade grave")
