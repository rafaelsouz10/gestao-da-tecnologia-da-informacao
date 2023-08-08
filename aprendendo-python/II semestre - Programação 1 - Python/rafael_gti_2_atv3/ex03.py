a= float(input('Insira o valor de a: '))
if a==0:
    print('\nA=0, logo não é uma equação de segundo grau.\n')
    exit()

b= float(input('Insira o valor de b: '))
c= float(input('Insira o valor de c: '))

delta= ((b**2)-(4*a*c))**(1/2)

if delta<0:
    print(f'\nO valor de Delta: {delta} é negativo, logo não possui raizes reais\n')
elif delta==0:
    raiz1= (delta-b)/(2*a)
    print(f'\nDelta=0, logo só existe uma raiz.\nRaiz= {raiz1}\n')
else:
    raiz1= (-b+delta)/(2*a)
    raiz2= (-b-delta)/(2*a)
    print(f'\nRaiz 1= {raiz1}\nRaiz 2= {raiz2}')
