# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 9: Erros - Aula: 74 """

# 74. Trabalhando com o Try e Except com o input

# erros (try except)
    # excelentes para testes
    # nao realiza o 'stop' no programa
    # mensagens customizadas quando 

try:
    valor = int(input("Digite do valor do seu produto: "))    
    print(valor)
except ValueError:
    print("Digite somente numeros.")
    
else:
    print("usuario digitou valor correto.")
    resultado = valor * 2
    print(resultado)

print("Mais codigo abaixo")

