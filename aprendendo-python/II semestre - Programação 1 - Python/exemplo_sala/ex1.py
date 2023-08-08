num1= int(input('Insira um numero: '))
num2= int(input('Insira um numero maior: '))

cont_par=0
if num1==num2:
    print('\nSem números pares entre os números.\n')
elif num1<num2:
    while num1<num2:
        if num1%2==0:
            cont_par += 1
            num1 += 2
        else:
            cont_par += 1
            num1 += 1
    print(f'\n{cont_par} numeros pares.\n')
else:
    while num2<num1:
        if num2%2==0:
            cont_par= cont_par+1
            num2= num2+2
        else:
            cont_par= cont_par+1
            num2= num2+1
    print(f'\n{cont_par} numeros pares.\n')