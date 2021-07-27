# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 4: Python Basico - Aula: 16 """

# o andre tem 32 anos de idade e mora em são paulo

nome = input("Qual é o seu nome? ")
idade = str(input("Qual a sua idade? "))
cidade = input("Em qual cidade você mora?: ")

# print("O " + nome + " tem "+ str(idade) + " anos de idade e mora em " + cidade.title() + ".")
print("O " + nome.title().strip() + " têm "+ idade.strip() + " anos de idade e mora em " + cidade.title().strip() + ".")

