num = int(input(f'Insira o 1 numero: '))
menor = num

for i in range(2,7):
    num = int(input(f'Insira o {i} numero: '))
    if num < menor:
        menor = num

print(f'\nO numero {menor} é o menor')