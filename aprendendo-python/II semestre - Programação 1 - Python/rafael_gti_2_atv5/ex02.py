nome = input('Insira uma frase ou palavra: ')
nome= nome.replace(" ", "")
#print(nome)
if nome == nome[::-1]:
    print('Palíndromo')
else:
    print('Não é Palíndromo')