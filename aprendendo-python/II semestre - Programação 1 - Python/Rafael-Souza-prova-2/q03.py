signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
signo_pessoa = []
for i in range(10):
    niver = input(f'Insira sua data de nascimento no formato (dd/mm/aaaa) da {i+1}ª pessoa: ')
    ano = niver[-4::]
    cod_signo = int(ano)%12
    signo_pessoa.append(signos[cod_signo])
print(signo_pessoa)