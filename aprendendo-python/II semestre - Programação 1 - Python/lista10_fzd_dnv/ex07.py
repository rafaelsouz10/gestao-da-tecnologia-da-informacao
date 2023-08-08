kart = {}
min_tempo = []
for i in range(3):
    corredor = input(f'\nInsira o nome do {i+1} corredor: ')
    kart[corredor] = []
    for j in range(5):
        tempo = input(f'Insira o tempo (em segundos) da {j+1}ª volta de {corredor}: ')
        kart[corredor].append(tempo)
    min_tempo.append(min(kart[corredor]))

melhor_tempo = min(min_tempo)
for corredor, tempos in kart.items():
    for volta, tempo in enumerate(tempos):
        if melhor_tempo == tempo:
            print(f'\nMehor volta: {corredor} ({melhor_tempo} segundos), na {volta+1}ª volta.')
            break