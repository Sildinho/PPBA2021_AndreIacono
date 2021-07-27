# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 10: OOP (Python Object-Oriented Programming) - Aula: 81 """

# 81. Calculando a idade do funcionário

# classes
    # utilizamos para criar objetos (instances)
    # objetos sao partes dentro de uma class (instancias)
    # classes sao utilizadas para agrupas dados e funções, podendo reutilizar

    # class: frutas
    # objects: abacate, banana, ...

    # criando uma classe

from datetime import datetime

class Funcionarios:

    # funções
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome+" " + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# criando um objeto com parametros
usuario1 = Funcionarios('Elena', 'cabral', 1999)
usuario2 = Funcionarios('Carol', 'Silva', 1995)
usuario3 = Funcionarios('André', 'Iacono', 1975)

# impressões
print(Funcionarios.idade_funcionario(usuario1))  # melhor opção.
