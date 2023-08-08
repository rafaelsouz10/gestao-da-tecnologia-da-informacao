"""1. Faça um programa que dado um número inteiro escolhido pelo usuário, 
crie uma lista com todos os números pares entre 1 e o número dado, inclusive."""

lista = []
num = int(input('Digite um número: '))
for i in range(num+1):
    if i % 2 == 0:
        lista.append(i)
print(lista)
