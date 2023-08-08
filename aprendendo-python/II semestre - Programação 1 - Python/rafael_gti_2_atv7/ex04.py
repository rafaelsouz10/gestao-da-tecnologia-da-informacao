# 4- Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.
notas = []
for i in range(4):
    nota = float(input(f'Insira a {i+1}ª nota: '))
    notas.append(nota)
media = sum(notas)/len(notas)
for i in notas:
    print(f'{notas.index(i)+1}ª nota: {i}')
print(f'Média: {media}')
