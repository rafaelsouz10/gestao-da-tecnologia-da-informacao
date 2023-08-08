'''5- Faça um programa que permita que o usuário entre com diversos
nomes e telefone para cadastro, e crie uma lista com essas informações,
uma par por posição. O usuário finaliza a entrada quando o telefone
digitado for “0”.
Ao final, exiba a lista na tela.'''
nomes=[]; tel=[]
while True:
    nomes.append(input('\nInsira um nome: '))
    tel.append(input(f"Para finalizar a entrada de dados, digite '0'.\nInsira o telefone referente a {nomes[-1]}: "))
    if tel[-1]=='0':
        print('\nLista finalizada')
        for i,nome in enumerate(nomes[:-1]):
            print(f'{i+1} - Nome: {nome} Telefone: {tel[i]}')
        break
