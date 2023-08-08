hora_inicio= int(input('Insira a hora do inicio do jogo: '))
hora_fim= int(input('Insira a hora do fim do jogo: '))

if hora_inicio>24 or hora_fim>24:
    print('\nHoras Inexistentes.\n')
    exit()

if hora_inicio>hora_fim:    #para calcular caso foi de um dia para o outro
    hora_inicio=hora_inicio-24

duracao=hora_fim-hora_inicio

if duracao<=24:
    print(f'\nDuração de jogo de {duracao} horas.\n')
else:
    print(f'\nTempo de {duracao} exedido 24 horas.\n')