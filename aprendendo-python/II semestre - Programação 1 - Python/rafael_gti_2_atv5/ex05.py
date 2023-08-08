for i in range(1,6):
    num= input(f"Insira a {i}ª string contendo apenas 0's e 1's: ")
    cont=num.count('1')
    for letra in num:
        if letra != '1' and letra!='0':
            print(f'A {i}º string contém outro tipo de caracter. Digite apenas 0 e 1')
            break
    if letra != '1' and letra!='0':
        continue
    print(f'{num} --> {cont}\n')