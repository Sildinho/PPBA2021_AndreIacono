# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 10: OOP (Python Object-Oriented Programming) - Aula: 79 """

# 79. Criando Construtores

# classes
    # utilizamos para criar objetos (instances)
    # objetos sao partes dentro de uma class (instancias)
    # classes sao utilizadas para agrupas dados e funções, podendo reutilizar
    
    # class: frutas
    # objects: abacate, banana, ...

# criando uma classe
class Funcionarios:
    
    # funções
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento        

# criando um objeto com parametros
usuario1 = Funcionarios('Elena', 'cabral', '12/01/1999')
usuario2 = Funcionarios('Carol', 'Silva', '17/11/1996')
usuario3 = Funcionarios('André', 'Iacono', '17/11/1977')


# impressões
print(usuario1.nome)
print(usuario2.nome)
print(usuario3.sobrenome)
