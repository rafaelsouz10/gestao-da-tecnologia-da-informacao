lista_num = []
while True:
    num = input('Insira um número: ')
    if num == '':
        break
    lista_num.append(int(num))
print('\n')
for i, nume in enumerate(lista_num):
    print(f'Número {nume}  posição {i}')

maior = max(lista_num)
menor = min(lista_num)
print(f'\nO maior número inserido é {maior} e tá na posição {lista_num.index(maior)}')
print(f'O menor número inserido é {menor} e tá na posição {lista_num.index(menor)}')