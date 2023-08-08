"""9- Faça um programa que leia um número indeterminado de notas. Após esta entrada de
dados, faça o seguinte:
    Mostre a quantidade de notas que foram lidas.
    Exiba todas as notas na ordem em que foram informadas.
    Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
    Calcule e mostre a soma das notas.
    Calcule e mostre a média das notas.
    Calcule e mostre a quantidade de notas acimada média calculada."""
lista_notas = []
operacao = 'S'
while operacao == 'S':
    nota = float(input('Digite uma nota: '))
    lista_notas.append(nota)
    operacao = input('Digite S se deseja continuar: ').upper()

media = sum(lista_notas)/len(lista_notas)
nota_alta = []
for nota in lista_notas:
    if nota > media:
        nota_alta.append(nota)
print(f"""
Quantidade de notas: {len(lista_notas)}
Lista de notas: {lista_notas}
Lista de notas inversa""")
for i in lista_notas[::-1]:
    print(i)
print(f"""Soma das notas: {sum(lista_notas)}
Média das notas: {media}
Quantidade de notas acima da média: {len(nota_alta)}
""")
