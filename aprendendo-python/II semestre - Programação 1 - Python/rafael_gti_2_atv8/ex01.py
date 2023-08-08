"""1- Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e 
a segunda como a versão após alterações. Utilizando operações com conjuntos, seu programa deverá 
imprimir a lista de modificações entre essas duas versões, listando:
    os elementos que não mudaram;
    os novos elementos;
    os elementos que foram removidos."""
lista1 = {1, 2, 3, 4, 5}
lista2 = {1, 3, 5, 6, 7, 8, 9}
print(f"{lista1=}\n{lista2=}")
print(f"Elementos que não mudaram: {lista1.intersection(lista2)}")
print(f"Novos Elementos: {lista2.difference(lista1)}")
print(f"Elementos Removidos: {lista1.difference(lista2)}")