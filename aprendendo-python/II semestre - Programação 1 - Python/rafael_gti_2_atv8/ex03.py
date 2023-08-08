"""3- Faça um programa que lê uma lista com 15 elementos inteiros e verifica
a existência de um número x na lista. O programa deve mostrar a posição
(ou as posições) em que x aparece na lista."""

lista = []
for i in range(1, 6):
    lista.append(int(input(f"Insira o {i}º elemento inteiro: ")))
print(lista)
num = int(input('Verifique a existência de um número na lista: '))
print(f"Elemento {num} em: ")
for i in range(len(lista)):
    if num == lista[i]:
        print(f"posição {i}")
