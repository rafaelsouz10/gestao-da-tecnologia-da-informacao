'''7- Uma pista de Kart permite 5 voltas para cada um (3 corredores).
Escreva um programa que leia todos os tempos (em segundos) e os
guarde em um dicionário, onde a chave é o nome do corredor. Ao
final, diga de quem foi a melhor volta e em qual volta da prova.
Ex: Melhor volta: Fulano (30 segundos), na 2a volta.'''
import os
kart = {}

for i in range(1,4):    
    nome = input(f'Digite o nome do {i}º corredor: ')
    kart[nome] = []
    for volta in range(5):
        tempo = float(input(f'Insira o tempo (em segundos) da {volta+1}ª volta do corredor {nome}: '))
        kart[nome].append(tempo)  
    os.system('cls')

for nome, tempo in kart.items():
    print(nome, tempo)

melhor_volta= 1000000; melhor_corredor = ''; melhor_tempo = 10000

for nome, tempo in kart.items():
    for volta, tempo in enumerate(tempo):
        if tempo < melhor_tempo:
            melhor_tempo = tempo
            melhor_corredor = nome
            melhor_volta = volta+1
print(f'\nMelhor volta: {melhor_corredor} ({melhor_tempo} segundos), na {melhor_volta}ª volta.')