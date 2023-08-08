'''6- Crie um dicionário vazio filmes = {}. Utilize o nome de um filme
como chave. E, como valor, outro dicionário contendo o vilão (chave) e
o ano (chave) em que o filme foi lançado. Preencha 5 filmes. Após isso,
solicite o nome de um filme ao usuário, e caso exista no dicionário,
mostre as informações do mesmo, do contrário, mostre a mensagem
"Filme não encontrado!".'''
import os
filmes = {"Vingadores": {"vilao": "Thanos", "ano": 2012},
          "Batman": {"vilao": "Coringa", "ano": 2008},
          "Star Wars": {"vilao": "Darth Vader", "ano": 1977},
          "Harry Potter": {"vilao": "Lord Voldemort", "ano": 2001},
          "Matrix": {"vilao": "Agente Smith", "ano": 1999}}

while True:
    print('Lista de filmes\n')
    for filme in filmes:
        print(filme)

    filme_user = input('\nEscolha um filme acima para saber suas informações: ').title()
    print('\n',filmes.get(filme_user, "Filme não encontrado!"))
    
    if filme_user in filmes:
        break
    input()
    os.system('cls')