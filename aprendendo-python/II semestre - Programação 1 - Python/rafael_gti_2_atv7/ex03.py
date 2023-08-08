#3- Ler uma lista de 10 números reais e mostre-os na ordem inversa.
lista = []
for i in range(10):
    lista.append(float(input(f'Insira o {i+1}º número real: ')))
print(lista)
print(lista[::-1])
