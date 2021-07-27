# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 10: OOP (Python Object-Oriented Programming) - Aula: 77 """

# 77. Criando a sua primeira classe

# classes
    # utilizamos para criar objetos (instances)
    # objetos sao partes dentro de uma class (instancias)
    # classes sao utilizadas para agrupas dados e funções, podendo reutilizar
    
    # class: frutas
    # objects: abacate, banana, ...

# criando uma classe
class Funcionarios:
    nome = 'Elena'
    sobrenome = 'Cabral'
    data_nascimento = '12/01/1999'

# criando um objeto
usuario1 = Funcionarios()


print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)
