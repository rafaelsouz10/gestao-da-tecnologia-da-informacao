import random

lista = []

for i in range(10):
    #lista.append(int(input(f'Insira o {i+1} número inteiro: ')))
    lista.append(random.randint(1,50))
print(lista)

num = int(input('\nInsira um número inteiro: '))

lista_menor = []; lista_maior = []; lista_igual = []

for num_lista in lista:
    if num_lista > num:
        lista_maior.append(num_lista)
    elif num_lista < num:
        lista_menor.append(num_lista)
    elif num_lista == num:
        lista_igual.append(num_lista)

print(f'\nNúmeros do vetor maiores que {num} são:', end=' ')
for num_maior in lista_maior:
    print(num_maior, end=' ')  
print(f'\nQuantidade de Números no vetor que são menores que {num}: {len(lista_menor)}')
print(f'O {num} aparece no vetor {len(lista_igual)}x.')
