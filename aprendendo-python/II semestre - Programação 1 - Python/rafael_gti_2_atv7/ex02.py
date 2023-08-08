# 2- Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.
lista = []
for i in range(5):
    lista.append(int(input(f'Digite o {i+1} numero inteiro: ')))
for i in lista:
    print(f'numero {i} na posição {lista.index(i)}')

# for pos, num in enumerate(lista):
#     print(pos, num)
