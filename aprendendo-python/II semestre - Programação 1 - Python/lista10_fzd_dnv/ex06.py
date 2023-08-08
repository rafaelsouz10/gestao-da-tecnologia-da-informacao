filmes = {}

for i in range(2):
    filme = input(f'Insira o nome do {i+1}º filme: ')
    vilao = input(f'Insira o vilão do {filme}: ')
    ano = input(f'Insira o ano de lançamento do {filme}: ')
    filmes[filme] = {'vilão': vilao, 'ano': ano}

print('\nFilmes cadastrados: ')
for filme in filmes:
    print(filme)
    
escolha_filme = input('\nInsira o nome de um filme para saber suas informações: ')
print(filmes.get(escolha_filme, 'Filme não encontrado!'))