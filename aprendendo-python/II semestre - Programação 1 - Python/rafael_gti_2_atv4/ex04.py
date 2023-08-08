num = int(input('Verifique um número se é primo: '))
cont = 0

if num < 0:
    print('Número negativo não é primo.')
    exit()

for i in range(1, num+1):
    if num % i == 0:
        cont += 1

print(f'\nO número {num} foi divisível {cont} vezes.')

if cont == 2:       #contador para saber quantas vezes o número foi divisível
    print('Logo, ele é primo!')
else:
    print('Logo, NÃO é primo!')