from funcoesLista2 import *

agenda = {}
contador = 1

while True:
    opcao = menu()
    if opcao == '0':
        print('\nSaindo do programa...\n')
        break
    elif opcao == '1':
            cadastro(agenda, contador)
    elif agenda != {}: #diferente de agenda vazia        
        if opcao == '2':
            editar(agenda) 

        else:
            system('cls')
            print('\nOpção Inválida.\n')
            input('Aperte algo para retornar ao menu principal...')
    else:
        system('cls')
        print('\nAgenda Vazia. Impossível utilizar opção.\n')
        input('Aperte algo para retornar ao menu principal...')