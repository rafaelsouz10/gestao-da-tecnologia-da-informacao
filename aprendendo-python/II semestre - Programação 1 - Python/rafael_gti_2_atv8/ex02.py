"""2- Faça um programa que leia e monte duas listas de números inteiros
com 10 números cada. Depois de montadas gere uma terceira lista
formada pela subtração de cada elemento das duas listas lidas, uma
quarta lista formada pela soma das duas primeiras listas lidas e por último
uma quinta lista formada pela multiplicação das duas primeiras."""
import random

lista1 = []; lista2 = []; lista3 = []; lista4 = []; lista5 = []
for i in range(10):
    lista1.append(random.randint(1, 10))
    lista2.append(random.randint(1, 10))
    lista3.append(lista1[i]-lista2[i])
    lista4.append(lista1[i]+lista2[i])
    lista5.append(lista1[i]*lista2[i])
print(f"""
{lista1=}
{lista2=}
Subtração: {lista3=}
Soma: {lista4=}
Multiplicação: {lista5=}""")
