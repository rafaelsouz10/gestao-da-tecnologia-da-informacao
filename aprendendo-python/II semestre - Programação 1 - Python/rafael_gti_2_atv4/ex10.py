qtd_pessoas = int(input('Quantas pessoas deseja entrevistar: '))

qtd_sim = 0; qtd_nao = 0; masc_nao = 0; fem_sim = 0

for i in range(1, qtd_pessoas+1):
    print(f'\n----------- Entrevista {i} -----------')
    cliente = int(input(f'Cliente {i}, você gostou do produto? 1-SIM 2-NÃO: '))
    sexo = input('Qual o seu sexo? M-MASCULINO F-FEMININO: ')

    if sexo == 'M' or sexo == 'm' and cliente == 2:
        masc_nao += 1
    elif sexo == 'F' or sexo == 'f' and cliente == 1:
        fem_sim +=1    

    if cliente == 1:
        qtd_sim += 1
    elif cliente == 2:
        qtd_nao += 1
    
porc_fem_sim = fem_sim/qtd_pessoas*100
porc_masc_nao = masc_nao/qtd_pessoas*100

print(f'\n{qtd_sim} pessoa(s) responderam SIM.\n{qtd_nao} pessoa(s) responderam NÃO.')
print(f'\nPorcentagem Mulher que disse sim: {porc_fem_sim:.2f}%.')
print(f'\nPorcentagem de Homem que disse não: {porc_masc_nao:.2f}%.\n')