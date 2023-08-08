salario= float(input('Insira o salário: '))

if salario<=280:
    reajuste= salario*0.2
    print(f'\nO percentual de aumento: 20%')
elif 280<salario<=700:
    reajuste= salario*0.15
    print(f'\nO percentual de aumento: 15%')
elif 700<salario<1500:
    reajuste= salario*0.1
    print(f'\nO percentual de aumento: 10%')
else:
    reajuste= salario*0.05
    print(f'\nO percentual de aumento: 5%')

novo_salario= salario+reajuste
print(f"Salário antes do ajuste: R$ {salario:.2f}\nValor do Aumento: R$ {reajuste:.2f}\nO novo salário é R$ {novo_salario:.2f}\n")