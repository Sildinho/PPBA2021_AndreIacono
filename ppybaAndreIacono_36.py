# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 6: Controle de Fluxo - Aula: 36 """

# 36. Criando condições com While Loop

# loops dependentes de uma condição.
# publicar um produto com comissao de 10% se for acima de R$ 20.00

valor = float(input("Digite o valor do seu produto em R$: "))

while valor >= 20.00:
    comiss = (valor * 0.10)
    valor = comiss + valor
    print(f'\nComissão: R$ {comiss}')
    print(f'O valor final do seu produto será de R${valor}')
    break






