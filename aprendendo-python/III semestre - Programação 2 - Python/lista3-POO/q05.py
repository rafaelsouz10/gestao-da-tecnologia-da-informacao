'''5. Classe Pessoa: Crie uma classe que modele uma pessoa:
    Atributos: nome, idade, peso e altura;
    Métodos: envelhecer, engordar, emagrecer, crescer
        Obs.: Por padrão, a cada ano que nossa pessoa envelhece, 
        sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura    #metros
    
    def crescer (self, cm):
        self.altura += cm/100
    
    def envelhecer(self, anos):
        