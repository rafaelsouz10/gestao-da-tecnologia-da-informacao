"""6- Ler uma lista de 10 elementos inteiros e positivos. Criar uma segunda
lista da seguinte forma: os elementos de índice par receberão os
respectivos elementos divididos por 2; os elementos de índice ímpar
receberão os respectivos elementos multiplicados por 3. Imprima as duas
listas."""
import random
lista1=[]; lista2=[]

for i in range(10):
    lista1.append(random.randint(1,50))
    if lista1[i]%2==0:
        lista2.append(lista1[i]/2)
    else:
        lista2.append(lista1[i]*3)
print(lista1)
print(lista2)