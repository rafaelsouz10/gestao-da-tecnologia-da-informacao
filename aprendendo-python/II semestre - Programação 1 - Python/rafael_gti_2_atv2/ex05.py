print("""Em que turno você estuda?
    M - Matutino
    V - Vespertino
    N - Noturno    
    """)
turno= input(": ")

if(turno=='m' or turno =='M'):
    print('\nBom Dia!\n')

elif(turno=='v' or turno =='V'):
    print('\nBoa Tarde!\n')

elif(turno=='n' or turno =='N'):
    print('\nBoa Noite!\n')

else:
    print('\nValor Inválido.\n')