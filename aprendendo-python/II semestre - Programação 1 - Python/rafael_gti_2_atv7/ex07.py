"""7- Faça um programa que crie uma lista aleatoriamente. O tamanho da lista deve ser
informado pelo usuário.
Dica: Pesquise sobre a biblioteca random do Python."""
from random import randint
tamanho_lista= int(input('Insira o tamanho da lista: '))
lista_aleatoria= []
for i in range(tamanho_lista):
    lista_aleatoria.append(randint(0,100))
print(lista_aleatoria)