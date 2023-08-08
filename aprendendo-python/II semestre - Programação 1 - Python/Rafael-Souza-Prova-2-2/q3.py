idades = []; alturas = []

for i in range(20):
    idades.append(int(input(f'\nInsira a idade da {i+1}ª pessoa: ')))
    alturas.append(float(input(f'Insira a altura da {i+1}ª pessoa: ')))

media_altura = sum(alturas)/len(alturas)

qtd_menor_altura = 0
for i in range(len(idades)):
    if idades[i] > 16:
        if alturas[i] < media_altura:
            qtd_menor_altura += 1

print(f'\nMédia das alturas: {media_altura}')
print(f'{qtd_menor_altura} pessoas com mais de 16 anos possuem a altura inferior à média da altura de todos.')