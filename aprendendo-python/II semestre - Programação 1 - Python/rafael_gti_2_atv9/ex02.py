"""2- Faça um programa que peça para o usuário criar uma lista de cidades
(nome da cidade e o seu número de habitantes), de pelo menos 10
cidades. Após criar a lista, o programa deverá pesquisar e mostrar o nome
da cidade mais populosa seguida pelo seu número de habitantes."""
cidade=[]; populacao=[]
for i in range(9):
    cidade.append(input('Insira o nome de uma cidade: '))
    populacao.append(int(input(f'Insira número de habitantes de {cidade[i]}: ')))
for i in range(len(cidade)):
    print(f'Cidade: {cidade[i]}   População: {populacao[i]}')
maior= max(populacao)   #pega a populacao maior
populacao_maior= populacao.index(maior) #vai pegar o indice da populacao maior
print(f'{cidade[populacao_maior]} é a cidade mais poupulosa da lista com {maior} habitantes.')
