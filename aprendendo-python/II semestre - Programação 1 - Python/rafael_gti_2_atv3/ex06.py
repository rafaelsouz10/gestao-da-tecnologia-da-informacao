litros= float(input('Quantos litros irá querer? '))

combustivel= input("""
    G - Gasolina
    A - Alcóol

    Digite o caracter respectivo ao combustível desejado: """)

if combustivel=='g' or combustivel=='G':
    if litros<=20:
        total= litros*6.20
        desconto= total*0.04
    else: 
        total= litros*6.20
        desconto= total*0.06
elif combustivel=='a' or combustivel=='A':
    if litros<=20:
        total= litros*3.10
        desconto= total*0.03
    else: 
        total= litros*3.10
        desconto= total*0.05
else:
    print('\nCaracter Inválido.\n')
    exit()

total_desc= total-desconto
print(f'\nTotal a pagar: R$ {total_desc:.2f}.\n')