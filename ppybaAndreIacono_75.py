# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 9: Erros - Aula: 75 """

# 75. Adicionando o Else e Finally

# erros (try except)
    # excelentes para testes
    # nao realiza o 'stop' no programa
    # mensagens customizadas quando 

# finnaly continua compilando mesmo com erro.

try:
    valor = int(input("Digite do valor do seu produto: "))    
    print(valor)
except ValueError:
    print("Digite somente numeros.")

finally:
    print("codigo ok.")

print("Seguir compilando o codigo.")
