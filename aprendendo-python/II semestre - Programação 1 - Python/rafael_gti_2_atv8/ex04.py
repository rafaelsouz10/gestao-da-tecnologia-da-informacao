"""4- Faça um lista de compras (utilize listas). O usuário deve ter a
possibilidade (menu) de inserir, apagar e listar os valores da sua lista. Não
permita que o programa quebre com erros de índices inexistentes na lista."""
import os

compras = []

while True:
    os.system('cls')
    menu = input("""
         ===============================
                LISTA DE COMPRAS

         [1]Inserir um item          
         [2]Apagar um item           
         [3]Listar itens        
         [4]Sair da lista            
         ===============================
         Escolha o que deseja fazer: """)
    os.system('cls')
    if menu == '1':
        item = input("Insira um item a lista de compras: ")
        compras.append(item.lower())
        print(f"\n{item} adicionado a lista")
        input()
        os.system('cls')
    elif menu == '2':
        for indice, item in enumerate(compras):
            print(f'{indice+1} - {item}') 
        item = input("\nExclua um item da lista: ")
        if item in compras:
            compras.remove(item)
            print(f"\n{item.lower()} excluído!")
        else:
            print(f"\n{item} não encontrado na lista")
        input()
        os.system('cls')
    elif menu == '3':
        print(f"Há {len(compras)} itens na sua lista de compras\n")
        for indice, item in enumerate(compras):
            print(f'{indice+1} - {item}')     
        input()
        os.system('cls')
    elif menu == '4':
        print('Saindo da lista...')
        input()
        break
    else:
        print("Opção inválida!")
        input()
