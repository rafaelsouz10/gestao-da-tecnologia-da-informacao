agenda = {}

print('---- Agenda de Contatos ------\n')
i = 1
while True:
    cpf = input(f'Insira o CPF do {i}º contato: ')
    nome = input(f'Insira o nome do portador do CPF {cpf}: ')
    idade = input(f'Insira a idade de {nome}: ')
    telefone = input(f'Insira o telefone de {nome}: ')

    agenda[cpf] = [nome, idade, telefone]

    exit = input('\nCadastrar mais contatos? [1]-Sim [Qualquer outra tecla]-Não: ')
    if exit != '1':
        break;
print('\n----- Contatos Salvos na Agenda ------\n')
for cpf, dados in agenda.items():
    nome, idade, telefone = dados
    print(f"{cpf}: '{nome}' - {idade} - {telefone}")