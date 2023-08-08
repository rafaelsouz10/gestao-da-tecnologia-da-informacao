# find(/) primeiro barra e rfind(/)do fim pro primeiro p encontrar o segundo barra
nasc = input('Insira sua data de nascimento (dd/mm/aaaa): ')

# isdigit() verifica se a substring 'ano' é número
if len(nasc[6:11]) == 4 and nasc[6:11].isdigit() and int(nasc[6:11]) >= 0:
    if 1 <= int(nasc[:2]) <= 28:
        if nasc[2:6] == '/02/':
            print(f"{nasc[0:2]} de Fevereiro de {nasc[6:10]}")
            exit()
    if 1 <= int(nasc[:2]) <= 30:
        if nasc[2:6] == '/04/':
            print(f"{nasc[0:2]} de Abril de {nasc[6:10]}")
        elif nasc[2:6] == '/06/':
            print(f"{nasc[0:2]} de Junho de {nasc[6:10]}")
        elif nasc[2:6] == '/09/':
            print(f"{nasc[0:2]} de Setembro de {nasc[6:10]}")
        elif nasc[2:6] == '/11/':
            print(f"{nasc[0:2]} de Novembro de {nasc[6:10]}")
        else:
            print('Data de Nascimento InválidaA')
            exit()
    if 1 <= int(nasc[:2]) <= 31:
        if nasc[2:6] == '/01/' and int(nasc[:2]) <= 31:
            print(f"{nasc[0:2]} de Janeiro de {nasc[6:10]}")
        elif nasc[2:6] == '/03/' and int(nasc[:2]) <= 31:
            print(f"{nasc[0:2]} de Março de {nasc[6:10]}")
        elif nasc[2:6] == '/05/':
            print(f"{nasc[0:2]} de Maio de {nasc[6:10]}")
        elif nasc[2:6] == '/07/':
            print(f"{nasc[0:2]} de Julho de {nasc[6:10]}")
        elif nasc[2:6] == '/08/':
            print(f"{nasc[0:2]} de Agosto de {nasc[6:10]}")
        elif nasc[2:6] == '/10/':
            print(f"{nasc[0:2]} de Outubro de {nasc[6:10]}")
        elif nasc[2:6] == '/12/':
            print(f"{nasc[0:2]} de Dezembro de {nasc[6:10]}")
        else:
            print('Data de Nascimento InválidaB')
            exit()
    if int(nasc[:2])>31 or int(nasc[:2])<1:
        print('Data de Nascimento InválidaC')
else:
    print('Data de Nascimento Inválida')
