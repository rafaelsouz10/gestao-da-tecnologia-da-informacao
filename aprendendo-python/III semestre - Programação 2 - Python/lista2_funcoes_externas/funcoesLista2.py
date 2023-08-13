from os import system

def menu():
    system('cls')
    print(f'''{"-"*50}
            MENU AGENDA
{"-"*50}

    [1] Cadastrar contatos
    [2] Editar contato
    [3] Excluir contato
    [4] Pesquisar contato pelo nome
    [5] Ordenar por ID
    [6] Ordenar por nomes
    [0] Sair do programa
{"-"*50}''')
    
    return input('Insira uma opção do MENU: ')

def cadastro(agenda, contador):
    system('cls')
    print(f'''{"-"*50}
            CADASTRAR CONTATO\n{"-"*50}''')   

    nome = input('Insira o nome do contato: ').title()
    endereco = input(f'Insira o endereco de {nome}: ').title()
    contato = input(f'Insira o contato de {nome}: ')
    
    agenda[str(contador)] = [nome, endereco, contato]
    contador +=1

    print('\nCadastro Concluído.\n')
    print(f'{"-"*50}')
    input('Aperte algo para retornar ao menu principal...')

    return agenda, contador

def editar(agenda):
    system('cls')
    print(f'''{"-"*50}
            EDITAR CONTATO\n{"-"*50}''')
    contato_id = input('Insira o ID do contato que deseja editar: ')
    for contato_id in agenda:
        print('1 - Nome:', agenda[contato_id][0])
        print('2 - Endereço:', agenda[contato_id][1])
        print('3 - Telefone:', agenda[contato_id][0])
        print('0 - Sair')
    opcao = input('O que deseja editar? ')

    if opcao == '1':
        nome = input('\nDigite o novo nome: ')
        agenda[contato_id][0] = nome
        print('\nContato Atualizado com sucesso.')
    elif opcao == '2':
        endereco = input('\nDigite o novo endereco: ')
        agenda[contato_id][1] = endereco
        print('\nContato Atualizado com sucesso.')
    elif opcao == '3':
        telefone = input('Digite o novo contato: ')
        agenda[contato_id][2] = telefone
        print('\nContato Atualizado com sucesso.')
    else:
        input('\nAperte algo para retornar ao menu principal...\n')
    return agenda

def excluir(agenda):
    system('cls')
    print(f'''{"-"*50}
            EXCLUIR CONTATO\n{"-"*50}''')
    contato_id = input('Insira o ID do contato que deseja excluir: ')
    for contato_id in agenda:
        print("ID:", contato_id)
        print("Nome:", agenda[contato_id][0])
        print("End:", agenda[contato_id][1])
        print("Tel:", agenda[contato_id][2])
    
    opcao = input('Qual contato deseja excluir? ')
    if opcao == '1':
        