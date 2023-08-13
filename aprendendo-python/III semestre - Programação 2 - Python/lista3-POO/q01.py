"""1. Classe Triangulo: Crie uma classe que modele um triângulo:
– Atributos: lado_A, lado_B, lado_C
– Métodos: calcular_perimetro, get_maior_lado;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um triângulo. 
Depois, deve criar um objeto com as medidas e imprimir seu perímetro e maior lado."""

class triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    
    def get_maior_lado(self):
        lado = [self.ladoA, self.ladoB, self.ladoC]
        return max(lado)

lado1 = float(input('Insira o primero lado: '))
lado2= float(input('Insira o segundo lado: '))
lado3 = float(input('Insira o terceiro lado: '))

if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
    triangulo1 = triangulo(lado1, lado2, lado3)
    print('Perímetro: ', triangulo1.calcular_perimetro())
    print('Maior Lado', triangulo1.get_maior_lado())
else:   
    print('Nâo formam um triângulo.')
