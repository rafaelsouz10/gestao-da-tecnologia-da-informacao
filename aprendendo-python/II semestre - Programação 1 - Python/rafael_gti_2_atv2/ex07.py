print("""Digite um número abaixo para o correpondente ao mês
1	-	janeiro
2	-	fevereiro
3	-	março	
4	-	abril
5	-	maio
6	-	junho
7	-	julho
8	-	agosto
9	-	setembro
10	-	outubro
11	-	novembro
12	-	dezembro
    """)
mes= float(input(": "))

if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    print('\nO mês tem 31 dias.\n')
elif mes==4 or mes==6 or mes==9 or mes==11:
    print('\nO mês tem 30 dias.\n')
elif mes==2:
    print('\nO mês tem 31 dias.\n')
else:
    print('Valor Inválido.')