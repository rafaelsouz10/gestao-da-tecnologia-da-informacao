idade= int(input('''
    Infantil A = 5 - 7 anos
    Infantil B = 8 - 10 anos
    Juvenil A = 11 - 13 anos
    Juvenil B = 14 - 17 anos
    Adulto = maiores 18 anos

    Insira a idade para saber sua categoria: '''))

if 5<=idade<=7:
    print('\nInfantil A = 5 - 7 anos\n')
elif 8<=idade<=10:
    print('\nInfantil B = 8 - 10 anos\n')
elif 11<=idade<=13:
    print('\nJuvenil A = 11 - 13 anos\n')
elif 14<=idade<=17:
    print('\nJuvenil B = 14 - 17 anos\n')
elif idade>=18:
    print('\nAdulto = maiores 18 anos\n')
else:
    print('\nIdade Inválida.\n')