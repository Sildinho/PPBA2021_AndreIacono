# -- coding utf-8 --
""" Udemy - Programação Python do Básico ao Avançado 2021 - Andre Iacono - Seção 10: OOP (Python Object-Oriented Programming) - Aula: 80 """

# 80. Adicionando mais funções a classe

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

    def nome_completo(self):
        return self.nome+" "+ self.sobrenome        

# criando um objeto com parametros
usuario1 = Funcionarios('Elena', 'cabral', '12/01/1999')
usuario2 = Funcionarios('Carol', 'Silva', '17/11/1996')
usuario3 = Funcionarios('André', 'Iacono', '17/11/1975')

# impressões
print(usuario1.nome+" "+usuario1.sobrenome)

print(f'{usuario1.nome} {usuario1.sobrenome}')

print(usuario1.nome_completo())

print(Funcionarios.nome_completo(usuario1)) # melhor opção.
