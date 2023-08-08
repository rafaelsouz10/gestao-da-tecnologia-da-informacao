"""2. Faça um programa que dada uma lista com 5 notas, retorne a maior e menor nota, a média das notas. 
Obs.: NÃO utilize as funções próprias do Python: len(), max(), min()."""
lista = [5.0, 2.0, 10.0, 1.5, 7.0]
maior = menor = lista[0]
for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
print(f'{maior = } {menor = }')