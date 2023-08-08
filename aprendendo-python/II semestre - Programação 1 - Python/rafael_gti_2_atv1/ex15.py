ganho_hr = float(input("Quanto você ganha por hora? "))
hr_mes = float(input("Quantas horas você trabalhou esse mês? "))

salario_bruto= ganho_hr*hr_mes
ir= salario_bruto*0.11
inss= salario_bruto*0.08
sindicato= salario_bruto*0.05
descontos= ir+inss+sindicato
salario_liquido= salario_bruto-descontos

print(f"""\n
    Salário BRUTO por hora trabalhada no mês: R$ {salario_bruto})
    Taxa paga ao Imposto de Renda (11%): R$ {ir}.
    Taxa paga ao INSS (8%): R$ {inss}.
    Taxa paga ao Sindicato (5%): R$ {sindicato}
    Salário LÍQUIDO por hora trabalhada no mês: R$ { salario_liquido}.
    \n\n""")