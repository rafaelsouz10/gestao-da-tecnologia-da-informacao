"""2. Classe Funcionario: Implemente a classe Funcionario.
Um funcionário tem os atributos nome e salário. Deve ter um método aumentar_salario(percentual) que aumente
 o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
Faça um programa que teste o método da classe."""

class Funcionario:
    def __init__(self, nome, salario, porcentagem):
        self.nome = nome
        self.salario = salario
        self.porcentagem = porcentagem
    
    def aumento_salario(self):
        self.salario += self.porcentagem/100*self.salario
        return self.salario

nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: '))
aumento = float(input('Digite quantos por cento de aumento do salário: '))

funcionario1 = Funcionario(nome, salario, aumento)
print(f'O salário de {nome}, com R$ {salario} com aumento de {aumento}%. Recebendo então R$ {funcionario1.aumento_salario():.2f}')