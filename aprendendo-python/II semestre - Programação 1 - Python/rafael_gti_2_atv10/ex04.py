'''4- Crie um dicionário que é uma agenda de contatos, e coloque nele os seguintes dados: 
cpf (chave), nome, idade, telefone. O programa deve solicitar ao usuário um número indeterminado
de contatos, criar a agenda e imprimir todos os itens do dicionário no 
formato --> cpf:nome – idade - telefone.
Ex:
    agenda = { "017785368": ["Caio", 18, 99999], ... }
Exibição:
    "017785368": "Caio" - 18 - 99999
...'''
import os

agenda = {}
while True:
    print('AGENDA DE CONTATOS\n')
    cpf = input('Insira um CPF: ')
    nome = input(f'Insira o nome do portador do CPF {cpf}: ')
    idade = input(f'Insira a idade de {nome}: ')
    telefone = input(f'Insira o telefone de {nome}: ')
    agenda[cpf] = [nome, idade, telefone]

    sair = input('\nDigite [1] para adicionar mais contatos a agenda\nCaso contrário, quaquer tecla: ')
    if sair != '1':
        break;
    os.system('cls')
os.system('cls')
print('CONTATOS DA AGENDA:\n')
for cpf, dados in agenda.items():
    nome, idade, telefone = dados
    print(f"'{cpf}': '{nome}' - {idade} - {telefone}")