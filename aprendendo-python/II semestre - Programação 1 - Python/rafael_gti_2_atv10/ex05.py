'''5- Crie um dicionário vazio semana = {} e o complete com uma chave
para cada dia da semana, tendo como seu valor uma lista com as aulas
que você tem nesse dia (sábado e domingo recebem listas vazias, ou
você tem aula?). Após, solicite ao usuário um dia da semana, e retorne
as aulas desses respectivo dia.'''
import os
semana = {'domingo': [],
          'segunda': [],
          'terça': [],
          'quarta': [],
          'quinta': [],
          'sexta': [],
          'sábado': [],
          }

print('AGENDA DO ESTUDANTE\n')
for dia in semana:
    dia_aula = input(f'Você tem aula no(a) {dia}: [1]-Sim [qualquer outra tecla]-Não: ')
    if dia_aula == '1':
        qtd_aula = int(input('Quantas aulas tem nesse dia? '))
        for i in range(1, qtd_aula+1):
            aula = input(f'Digite a aula do {i}º horário: ')
            semana[dia].append(aula)
    else:
        semana[dia].append('Sem aula')
    os.system('cls')
print('HORÁRIO DE AULA CADASTRADAS\n')
for dia, aulas in semana.items():
    print(dia)
    for aula in aulas:
        print(f'    {aulas.index(aula)+1}ª aula: {aula}')
input("\nAperte qualquer telca pra continuar...")
os.system('cls')

while True:
    print('Dias da semana\n')
    for dia in semana:
        print(dia)
    dia_user = input('\nInsira um dia da semana para saber suas respectivas aulas: ')

    if dia_user not in semana:
        print('Dia não encontrado...')
        input()
        os.system('cls')
        continue
    for horario, aula in enumerate(semana[dia_user]):
        print(f'{horario+1}ª horário: {aula}')
    exit = input('\nInsira [1]- Consultar outro dia [Qualquer outra tecla]-Sair: ')
    if exit != '1':
        break
    os.system('cls')