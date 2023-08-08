vetor = [2.0, 7.5, 8.0, 4.2, 8.3]
media = sum(vetor)/len(vetor)
prox = []

for i in vetor:
    i = media-i
    if i<0:
        i *= -1
    prox.append(i)
indice = prox.index(min(prox))
print(f'Valor mais próximo da média: {vetor[indice]}')