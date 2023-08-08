num1= float(input('Insira um numero: '))
num2= float(input('Insira outro numero: '))

operacao= input("""
    1- par ou ímpar
    2- positivo ou negativo
    3- inteiro ou decimal
    Qual operação quer fazer:""")

if operacao=='1':
    if num1%2 == 0:
        print(f'\n{num1} é par\n')
    else:
        print(f'{num1} é ímpar\n')
        
    if num2%2 == 0:
        print(f'\n{num2} é par\n')
    else:
        print(f'{num2} é ímpar\n')

elif operacao=='2':
    if num1>=0:
        print(f'\n{num1} é positivo\n')
    else:
        print(f'\n{num1} é negativo\n')
    if num2>=0:
        print(f'\n{num2} é positivo\n')
    else:
        print(f'\n{num2} é negativo\n')

elif operacao=='3':
    if num1==int(num1):
        print(f'\n{int(num1)} é Inteiro\n')
    else:
        print(f'\n{num1} é Decimal\n')
    if num2==int(num2):
        print(f'\n{int(num2)} é Inteiro\n')
    else:
        print(f'\n{num2} é Decimal\n')
else:
    print('\nOperação Inválida.\n')