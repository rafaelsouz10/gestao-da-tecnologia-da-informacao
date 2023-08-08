lado1= float(input("Insira o primeiro lado do triangulo: "))
lado2= float(input("Insira o segundo lado do triangulo: "))
lado3= float(input("Insira o terceiro lado do triangulo: "))

if (lado1+lado2)>lado3 and (lado1+lado3)>lado2 and (lado2+lado3)>lado1:
    if lado1==lado2==lado3:
        print('\nTriângulo Equilátero.\n')
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print('\nTriângulo Isósceles.\n')
    else:
        print('\nTriângulo Escaleno.\n')
else:
    print('\nOs números digitados não formam um triângulo.\n')
