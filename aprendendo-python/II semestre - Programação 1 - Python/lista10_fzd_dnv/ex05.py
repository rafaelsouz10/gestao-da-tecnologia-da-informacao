semana = {}
dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')

for dia in dias:
    semana[dia] = []
    qtd_aula = int(input(f'Quantas aulas você {dia}? '))
    for aulas in range(qtd_aula):
        aula = input(f'Qual a {aulas+1}ª aula de {dia}? ')
        semana[dia].append(aula)
print('\n')
for dia in semana:
    print(dia)

escolha_dia = input('Insira um dia da semana para saber suas respectivas aulas: ').lower()

print(semana.get(escolha_dia, 'Dia não encontrado.'))