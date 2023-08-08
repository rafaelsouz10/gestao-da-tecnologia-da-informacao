salario= float(input('Insira seu salário: '))
vendas= int(input('Insira o valor total das vendas efetuadas: '))

if vendas<=1500:
    comissao= vendas*0.03
else:
    comissao= 1500*0.03
    comissao_extra= (vendas-1500)*0.05
    comissao= comissao+comissao_extra
salario= salario+comissao
print(f'\nO seu salário com comissão é R$ {salario:.2f}.\n')