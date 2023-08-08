nome= input('Insira o seu nome: ').upper()  #todas as letras em maiúsculo
posicao= nome.find(' ')     #find vai procurar a posição que o espaço vai tá
idade= int(input('Insira sua idade: '))
sexo= input('Insira seu sexo M-Masculino F-Feminino: ').lower() #deixa minúsculo

if sexo[0]=='f' and idade<25:
    
    print(nome[:posicao]+' ACEITA')
else:
    print('NÃO ACEITA')