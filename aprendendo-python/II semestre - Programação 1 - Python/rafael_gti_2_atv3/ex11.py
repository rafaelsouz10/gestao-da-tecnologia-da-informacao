nome= input('Insira o seu nome: ')
nasc= int(input('Insira o seu ano de nascimento: '))
ano_ing= int(input('Insira o ano de seu ingresso na empresa: '))


idade= 2023-nasc
temp_trabalho= 2023-ano_ing
print(f"""
Empregado: {nome}.
Idade: {idade} anos.
Tempo de Trabalho: {temp_trabalho}.""")

if idade>=temp_trabalho:
    if idade>=65 or temp_trabalho>=30 or (idade>=60 and temp_trabalho>=25):
        print('Requerer Aposentadoria.\n')
    else:
        print('Não Requerer.\n')
else:
    print('\nDados incompatíveis.\n') #caso o tempo de trabalho for maior que a idade