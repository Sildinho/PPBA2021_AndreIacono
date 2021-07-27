# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 10: OOP (Python Object-Oriented Programming) - Aula: 78 """

# 78. Criando Objetos dentro de uma Classe

# classes
    # utilizamos para criar objetos (instances)
    # objetos sao partes dentro de uma class (instancias)
    # classes sao utilizadas para agrupas dados e funções, podendo reutilizar
    
    # class: frutas
    # objects: abacate, banana, ...

# criando uma classe
class Funcionarios:
    pass

# criando um objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# criando parametros do usuario1
usuario1.nome = 'Elena'
usuario1.sobrenome = 'cabral'
usuario1.data_nascimento = '12/01/1999'

# criando parametros do usuario2
usuario2.nome = 'Carol'
usuario2.sobrenome = 'Silva'
usuario2.data_nascimento = '17/11/1996'

# impressões
print(usuario1.nome)
print(usuario2.nome)
