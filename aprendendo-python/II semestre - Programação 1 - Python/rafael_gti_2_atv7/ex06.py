"""6- Ler uma lista com 20 idades e exibir a maior e menor."""
idades = []
for i in range(20):
    idade= int(input(f'Insira a {i+1}ª idade: '))
    idades.append(idade)
print(idades)
print(f'Maior idade: {max(idades)}\nMenor idade: {min(idades)}')
