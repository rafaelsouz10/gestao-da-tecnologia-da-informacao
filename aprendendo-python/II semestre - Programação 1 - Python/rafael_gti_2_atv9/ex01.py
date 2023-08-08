"""1- Escreva um programa que permita o usuário escrever uma mensagem
na tela e guarde tudo em uma string. A escrita só vai parar quando o
usuário entrar com o caractere “0”;
Logo após, mostre a string gerada."""

mensagem=[]
mensagem.append(input('Insira uma mensagem: '))
while True:
    para = input("\nDigite '0' para terminar a escrita: ")
    if para=='0':
        print(' '.join(mensagem))
        break
    else:
        mensagem.append(input('\nContinue a mensagem: '))