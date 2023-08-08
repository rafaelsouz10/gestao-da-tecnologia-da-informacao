"""4. Faça um programa que dadas duas listas de três elementos com números inteiros, 
crie uma lista onde cada elemento é a soma das posições cruzadas. 
Exemplo:
    Lista1 = [1 ,4 ,6]
    Lista2 = [2 ,5 ,3]
    Lista resultante = [8, 9, 4]"""
lista1 = [1 ,4 ,6]; lista2 = [2 ,5 ,3]
resultante = [lista1[2]+lista2[0], lista1[1]+lista2[1], lista1[0]+lista2[2]]
print(f'{lista1 = }\n{lista2 = }\n{resultante = }')