"""5- Desenvolva um programa que armazene quatro notas em uma lista e que apresente a
média final. Caso a média seja igual ou superior a 7, apresentar a mensagem
"APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média. Caso a
nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário,
apresentar a mensagem "REPROVADO"."""
notas = []
for i in range(4):
    nota= float(input(f'Insira a {i+1}ª nota: '))
    notas.append(nota)
media= sum(notas)/len(notas)
print(f'Média: {media}')
if media>=7:
    print('APROVADO ')
else:
    nota_final= float(input('Insira a nota da prova final: '))
    if nota_final>=5:
        print('APROVADO')
    else:
        print('REPROVADO')